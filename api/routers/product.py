from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from api.controllers import product_controller
from api.db.database import SessionDep
from api.models.product import Product, ProductCreate, ProductPublic, ProductUpdate

router = APIRouter(prefix="/product", tags=["products"])


# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductPublic)
async def create_product(product: ProductCreate, session: SessionDep) -> ProductPublic:
    """Add the product to the database."""
    try:
        validated_product = Product.model_validate(product)
        return await product_controller.create_product(validated_product, session)
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not process the input product: {product}, {e}",
        ) from e


# Read
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProductPublic])
async def get_products(session: SessionDep) -> list[ProductPublic]:
    """Return all products in the database."""
    return await product_controller.get_products(session)


@router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: UUID, session: SessionDep) -> ProductPublic:
    """Get a product by id, if it is present - otherwise error."""
    return await product_controller.get_product_by_id(product_id, session)


# Update
@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(
    product_id: UUID, product_update: ProductUpdate, session: SessionDep
) -> ProductPublic:
    """Update a product based on the given fields."""
    return await product_controller.update_product(product_id, product_update, session)


# Update
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID, session: SessionDep) -> None:
    """Delete a product based on id."""
    await product_controller.delete_product(product_id, session)
