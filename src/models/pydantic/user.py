from typing import Annotated

from pydantic import BaseModel


class User(BaseModel):
    first_name: Annotated[str, "First name"]
    last_name: Annotated[str, "Last name"]
    email: Annotated[str, "Email"]
