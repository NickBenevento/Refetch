from typing import Annotated

from pydantic import AliasChoices, AfterValidator, BaseModel


def validate_email(value: str):
    # Check that email is valid
    return value

class User(BaseModel):
    # Keep the actual field name in the aliases 
    first_name: Annotated[str, "First name", AliasChoices('first_name', 'fname', 'first')]
    last_name: Annotated[str, "Last name", AliasChoices('last_name', 'lname', 'last', 'surname', 'family_name')]
    email: Annotated[str, AfterValidator(validate_email), "Email"]
