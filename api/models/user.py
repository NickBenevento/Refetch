import uuid
from typing import Annotated

from pydantic import AliasChoices, EmailStr
from sqlmodel import Field, SQLModel, String


class UserBase(SQLModel):
    # "index=True" creates a SQL index for the column - faster DB lookups
    first_name: Annotated[
        str,
        Field(index=True),
        "First name",
        AliasChoices("first_name", "fname", "first"),
    ]
    last_name: Annotated[
        str,
        Field(index=True),
        "Last name",
        AliasChoices("last_name", "lname", "last"),
    ]
    email: Annotated[
        EmailStr,
        Field(index=True, sa_type=String),
        "Email",
    ]


class User(UserBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)


class UserCreate(UserBase):
    pass


class UserPublic(UserBase):
    id: uuid.UUID


class UserUpdate(UserBase):
    first_name: Annotated[
        str | None,
        Field(default=None),
        "Updated first name",
    ]
    last_name: Annotated[
        str | None,
        Field(default=None),
        "Updated last name",
    ]
    email: Annotated[
        EmailStr | None,
        Field(default=None),
        "Updated email",
    ]
