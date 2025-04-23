import uuid
from typing import Annotated

import validators
from pydantic import AfterValidator, BaseModel, Field, ValidationError


def check_valid_url(url: str) -> str:
    if not validators.url(url):
        raise ValidationError("Invalid url: %s", url)
    return url


class Product(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    url: Annotated[
        str, AfterValidator(check_valid_url), "The url to the desired product page"
    ]

    name: Annotated[str, "The name of the product"]


class ProductList(BaseModel):
    products: list[Product]
