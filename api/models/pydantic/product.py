import uuid
from typing import Annotated

from pydantic import AnyUrl, BaseModel, Field


class Product(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    url: Annotated[AnyUrl, "The url to the desired product page"]

    name: Annotated[str, "The name of the product"]


class UpdateProduct(BaseModel):
    url: Annotated[AnyUrl | None, "The new url"]
    name: Annotated[str | None, "The new name of the product"]


class ProductList(BaseModel):
    products: list[Product]
