import uuid
from typing import Annotated

from pydantic import AfterValidator, AliasChoices
from sqlmodel import Field, SQLModel


def validate_email(value: str):
    # Check that email is valid
    return value


class User(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    # "index=True" creates a SQL index for the column - faster DB lookups
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    first_name: str = Annotated[
        str,
        Field(index=True),
        "First name",
        AliasChoices("first_name", "fname", "first"),
    ]
    last_name: str = Annotated[
        str,
        Field(index=True),
        "Last name",
        AliasChoices("last_name", "lname", "last"),
    ]
    email: str = Annotated[
        str, AfterValidator(validate_email), Field(index=True), "Email"
    ]
