from uuid import UUID

from fastapi import HTTPException
from fastapi.exceptions import ResponseValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from api.db.database import SessionDep
from api.models.user import User, UserPublic, UserUpdate


async def create_user(user: User, session: SessionDep) -> UserPublic:
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except IntegrityError as e:
        raise HTTPException(
            status_code=500, detail="An integrity error occurred: {e}"
        ) from e
    return user


async def get_users(session: SessionDep) -> list[UserPublic]:
    try:
        users = session.exec(select(User)).scalars().all()
        return users
    except IntegrityError as e:
        raise HTTPException(
            status_code=500, detail="An integrity error occurred: {e}"
        ) from e
    except ResponseValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the output: {users}, {e}",
        ) from e


async def get_user_by_id(user_id: UUID, session: SessionDep) -> User:
    try:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=404, detail=f"user with id {user_id} not found"
            )
        return user
    except ResponseValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the output: {user}, {e}",
        ) from e


async def update_user(
    user_id: UUID, user_update: UserUpdate, session: SessionDep
) -> UserPublic:
    user: UserPublic = await get_user_by_id(user_id=user_id, session=session)
    if user_update.first_name:
        user.first_name = user_update.first_name
    if user_update.last_name:
        user.last_name = user_update.last_name
    if user_update.email:
        user.email = user_update.email

    session.add(user)
    session.commit()
    return user


async def delete_user(user_id: UUID, session: SessionDep) -> None:
    user = await get_user_by_id(user_id, session)
    session.delete(user)
    session.commit()
