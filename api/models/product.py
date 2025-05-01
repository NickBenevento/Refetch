import uuid
from typing import Annotated

from pydantic import AfterValidator, AnyUrl
from sqlmodel import Field, SQLModel


def validate_email(url: str) -> str:
    _: AnyUrl = AnyUrl(url)
    return url


class ProductBase(SQLModel):
    url: str = Field(
        AfterValidator(validate_email),
        title="The url to the desired product page",
        index=True,
    )

    name: str = Field("The name of the product", index=True)


class Product(ProductBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)


class ProductCreate(ProductBase):
    pass


class ProductPublic(ProductBase):
    id: uuid.UUID


class ProductUpdate(ProductBase):
    url: Annotated[AnyUrl | None, Field(default=None), "The new url"]
    name: Annotated[str | None, Field(default=None), "The new name of the product"]
