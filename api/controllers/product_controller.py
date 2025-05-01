from fastapi import HTTPException
from fastapi.exceptions import ResponseValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from api.db.database import SessionDep
from api.models.product import Product, ProductBase, ProductPublic


async def create_product(product: ProductBase, session: SessionDep) -> ProductPublic:
    try:
        session.add(product)
        session.commit()
        session.refresh(product)
    except IntegrityError as e:
        raise HTTPException(
            status_code=500, detail="An integrity error occurred: {e}"
        ) from e
    return product


async def get_products(session: SessionDep) -> list[ProductPublic]:
    try:
        products = session.exec(select(Product)).scalars().all()
        return products
    except IntegrityError as e:
        raise HTTPException(
            status_code=500, detail="An integrity error occurred: {e}"
        ) from e
    except ResponseValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the output: {products}, {e}",
        ) from e
