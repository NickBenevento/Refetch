import uuid
from typing import Annotated

from pydantic import BeforeValidator, ConfigDict, HttpUrl, TypeAdapter
from sqlmodel import AutoString, Field, SQLModel

http_url_adapter = TypeAdapter(HttpUrl)


class ProductBase(SQLModel):
    url: Annotated[
        str,
        BeforeValidator(lambda value: str(http_url_adapter.validate_python(value))),
        Field(..., index=True),
        "The url to the desired product page",
    ]

    name: Annotated[
        str,
        Field(..., index=True),
        "The name of the product",
    ]

    model_config = ConfigDict(
        from_attributes=True,
        # json_schema_extra={
        #     "example": {"url": "https://example.com", "name": "Product Name"}
        # },
    )


class Product(ProductBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)


class ProductCreate(ProductBase):
    pass


class ProductPublic(ProductBase):
    id: uuid.UUID


class ProductUpdate(ProductBase):
    url: Annotated[HttpUrl | None, Field(default=None), "The new url"]
    name: Annotated[str | None, Field(default=None), "The new name of the product"]
