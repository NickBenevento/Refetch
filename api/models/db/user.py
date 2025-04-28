import uuid
from typing import Annotated

from pydantic import AfterValidator, AliasChoices
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlmodel import Field, SQLModel

from api.models.db.base import Base


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


class User2(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(50))

    # TODO: add relationship to "subscription" table

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r} {self.last_name!r}, email={self.email!r})"
