import uuid
from typing import Annotated

from pydantic import AfterValidator, AnyUrl, BaseModel, Field
from sqlmodel import Field, SQLModel


def validate_email(email: str) -> bool:
    test_email: AnyUrl = AnyUrl(email)
    return True


class Product(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)

    # url: Annotated[AnyUrl, Field(index=True), "The url to the desired product page"]
    url: Annotated[
        str,
        AfterValidator(validate_email),
        Field(index=True),
        "The url to the desired product page",
    ]

    name: Annotated[str, Field(index=True), "The name of the product"]


class UpdateProduct(BaseModel):
    url: Annotated[AnyUrl | None, "The new url"]
    name: Annotated[str | None, "The new name of the product"]


class ProductList(BaseModel):
    products: list[Product]
