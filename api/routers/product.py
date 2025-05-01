from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from api.controllers import product_controller
from api.db.database import SessionDep
from api.models.product import Product, ProductBase, ProductPublic, ProductUpdate

router = APIRouter(prefix="/products", tags=["products"])


# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductBase, session: SessionDep) -> ProductPublic:
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


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(item_id: UUID) -> Product:
    """Get a product by id, if it is present - otherwise error."""
    # get product by id from db
    # if not item_id
    #
    return {"products": "all products"}


# Update
@router.put("/", status_code=status.HTTP_200_OK)
async def update_product(product_update: ProductUpdate) -> Product:
    """Update a product based on the given fields."""
    # TODO: update database
    return {}


# Update
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(item_id: UUID):
    """Delete a product based on id."""
    # TODO: update database
    # get product by id from db
    # if not item_id
    return {}
