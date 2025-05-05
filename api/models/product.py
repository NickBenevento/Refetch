import uuid
from typing import Annotated

from pydantic import AnyUrl, ConfigDict
from sqlmodel import AutoString, Field, SQLModel


class ProductBase(SQLModel):
    url: Annotated[
        AnyUrl,
        Field(index=True, sa_type=AutoString),
        "The new url to the desired product page",
    ]

    name: str = Field("The name of the product", index=True)

    model_config = ConfigDict(from_attributes=True)


class Product(ProductBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)


class ProductCreate(ProductBase):
    pass


class ProductPublic(ProductBase):
    id: uuid.UUID


class ProductUpdate(ProductBase):
    url: Annotated[AnyUrl | None, Field(default=None), "The new url"]
    name: Annotated[str | None, Field(default=None), "The new name of the product"]
