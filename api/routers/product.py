from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from api.db.database import SessionDep
from api.models.db.product import Product
from api.models.pydantic.product import UpdateProduct

router = APIRouter(prefix="/products", tags=["products"])


# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product, session: SessionDep) -> Product:
    try:
        session.add(product)
        session.commit()
        session.refresh(product)
    except IntegrityError as e:
        raise HTTPException(
            status_code=500, detail="An integrity error occurred: {e}"
        ) from e
    except SQLAlchemyError as e:
        print("SQLAlchemy error: %s", e)
        raise HTTPException(
            status_code=500, detail="SQLAlchemy error occurred: {e}"
        ) from e
    return product


# Read
@router.get("/", status_code=status.HTTP_200_OK)
async def get_products():

    return {"products": "all products"}


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(item_id: UUID):
    # get product by id from db
    # if not item_id
    #
    return {"products": "all products"}


# Update
@router.put("/", status_code=status.HTTP_200_OK)
async def update_product(update_product: UpdateProduct):
    # TODO: update database
    return {}


# Update
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(item_id: UUID):
    # TODO: update database
    # get product by id from db
    # if not item_id
    return {}
