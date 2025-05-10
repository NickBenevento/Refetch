import pytest


@pytest.fixture
def example_product() -> dict[str, str]:
    return {"url": "https://google.com/", "name": "google test"}
