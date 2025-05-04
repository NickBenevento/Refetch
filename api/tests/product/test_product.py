from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_get_products():
    response = client.get("/product/")
    assert response.status_code == 200
