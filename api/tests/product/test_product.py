import uuid


def test_get_products(client):
    response = client.get("/product/")
    assert response.status_code == 200


def test_create_product(client, example_product):
    response = client.post("/product/", json=example_product)
    assert response.status_code == 201
    created_product = response.json()
    assert created_product["url"] == example_product["url"]
    assert created_product["name"] == example_product["name"]


def test_create_product_invalid_url(client):
    product = {"url": "google", "name": "google test"}
    response = client.post("/product/", json=product)
    assert response.status_code == 422


def test_create_product_invalid_name(client):
    product = {"url": "google", "name": ""}
    response = client.post("/product/", json=product)
    assert response.status_code == 422


def test_get_product_by_id(session, client, example_product):
    result = client.post("/product/", json=example_product)
    product_id = result.json()["id"]

    response = client.get(f"/product/{product_id}")
    assert response.status_code == 200
    assert response.json()["url"] == example_product["url"]
    assert response.json()["name"] == example_product["name"]


def test_get_product_by_invalid_id(client):
    bad_id = 100
    response = client.get(f"/product/{bad_id}")
    assert response.status_code == 422
    bad_id = uuid.uuid4()
    response = client.get(f"/product/{bad_id}")
    assert response.status_code == 404


def test_update_product(session, client, example_product):
    pass
