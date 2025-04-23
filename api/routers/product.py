from fastapi import APIRouter, status

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_products():
    return {"products": "all products"}
