from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_get_products():
    response = client.get("/product/")
    assert response.status_code == 200


# TODO: set up mock db and conftest to create products
def test_get_product_by_id():
    response = client.get("/product/")
    assert response.status_code == 200


def test_create_product():
    product = {"url": "https://google.com/", "name": "google test"}
    response = client.post("/product/", json=product)
    assert response.status_code == 201
    created_product = response.json()
    assert created_product["url"] == product["url"]
    assert created_product["name"] == product["name"]


def test_create_product_invalid_url():
    product = {"url": "google", "name": "google test"}
    response = client.post("/product/", json=product)
    assert response.status_code == 422


def test_create_product_invalid_name():
    product = {"url": "google", "name": ""}
    response = client.post("/product/", json=product)
    assert response.status_code == 422


def test_update_product_invalid_name():
    product = {"url": "google", "name": ""}
    response = client.post("/product/", json=product)
    assert response.status_code == 422
