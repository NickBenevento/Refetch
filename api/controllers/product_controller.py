from uuid import UUID

from fastapi import HTTPException
from fastapi.exceptions import ResponseValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from api.db.database import SessionDep
from api.models.product import Product, ProductPublic, ProductUpdate


async def create_product(product: Product, session: SessionDep) -> ProductPublic:
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


async def get_product_by_id(product_id: UUID, session: SessionDep) -> Product:
    try:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(
                status_code=404, detail=f"Product with id {product_id} not found"
            )
        return product
    except ResponseValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the output: {product}, {e}",
        ) from e


async def update_product(
    product_id: UUID, product_update: ProductUpdate, session: SessionDep
) -> ProductPublic:
    product: ProductPublic = await get_product_by_id(
        product_id=product_id, session=session
    )
    if product_update.name:
        product.name = product_update.name
    if product_update.url:
        product.url = product_update.url

    session.add(product)
    session.commit()
    return product


async def delete_product(product_id: UUID, session: SessionDep) -> None:
    product = await get_product_by_id(product_id, session)
    session.delete(product)
    session.commit()
