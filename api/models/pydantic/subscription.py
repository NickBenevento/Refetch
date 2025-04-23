from typing import Annotated
from pydantic import AfterValidator, BaseModel


def validate_url(value: str):
    # Check to ensure the url is valid
    return value


class Subscription(BaseModel):
    name: Annotated[str, "The name to give the subscription"]
    url: Annotated[str, AfterValidator(validate_url)]

class SubscriptionList():
    subscriptions: Annotated[list[Subscription], "List of subscriptions"]
