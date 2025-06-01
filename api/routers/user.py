from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from api.controllers import user_controller
from api.db.database import SessionDep
from api.models.user import User, UserBase, UserCreate, UserPublic, UserUpdate

router = APIRouter(prefix="/user", tags=["users"])


# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserPublic)
async def create_user(user: UserCreate, session: SessionDep) -> UserPublic:
    """Add the user to the database."""
    try:
        validated_user = User.model_validate(user)
        return await user_controller.create_user(validated_user, session)
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the input user: {user}, {e}",
        ) from e


# Read
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserPublic])
async def get_users(session: SessionDep) -> list[UserPublic]:
    """Return all users in the database."""
    return await user_controller.get_users(session)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserPublic)
async def get_user_by_id(user_id: UUID, session: SessionDep) -> UserPublic:
    """Get a user by id, if it is present - otherwise error."""
    return await user_controller.get_user_by_id(user_id, session)


# Update
@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserPublic)
async def update_user(
    user_id: UUID, user_update: UserUpdate, session: SessionDep
) -> UserPublic:
    """Update a user based on the given fields."""
    return await user_controller.update_user(user_id, user_update, session)


# Update
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID, session: SessionDep) -> None:
    """Delete a user based on id."""
    await user_controller.delete_user(user_id, session)
