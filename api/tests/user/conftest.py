import pytest


@pytest.fixture
def example_user() -> dict[str, str]:
    return {"first_name": "Bill", "last_name": "Nye", "email": "thescienceguy@gmail.com"}
