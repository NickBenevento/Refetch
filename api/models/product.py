import uuid
from typing import Annotated

from pydantic import BeforeValidator, ConfigDict, Field, HttpUrl, TypeAdapter
from sqlmodel import Field, SQLModel

http_url_adapter = TypeAdapter(HttpUrl)


class ProductBase(SQLModel):
    # Need to save as a string (for DB purposed), but still want URL validation
    # Approach for this taken from here: https://github.com/pydantic/pydantic/discussions/6395
    url: Annotated[
        str,
        BeforeValidator(lambda value: str(http_url_adapter.validate_python(value))),
        Field(
            ...,
            index=True,
            description="The url to the desired product page",
        ),
    ]

    name: Annotated[
        str,
        Field(..., index=True),
        "The name of the product",
    ]

    model_config = ConfigDict(
        from_attributes=True,
    )


class Product(ProductBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)


class ProductCreate(ProductBase):
    url: HttpUrl


class ProductPublic(ProductBase):
    id: uuid.UUID
    url: HttpUrl


class ProductUpdate(ProductBase):
    url: Annotated[HttpUrl | None, Field(default=None), "The new url"]
    name: Annotated[str | None, Field(default=None), "The new name of the product"]
