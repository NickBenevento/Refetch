import uuid


def test_get_users(client):
    response = client.get("/user/")
    assert response.status_code == 200


def test_create_user(client, example_user):
    response = client.post("/user/", json=example_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["first_name"] == example_user["first_name"]
    assert created_user["last_name"] == example_user["last_name"]
    assert created_user["email"] == example_user["email"]


def test_create_user_invalid_email(client, example_user):
    example_user["email"] = "invalidemail.com"
    response = client.post("/user/", json=example_user)
    assert response.status_code == 422


def test_create_user_invalid_first_name(client, example_user):
    example_user["first_name"] = ""
    user = {"first_name": "", "last_name": "Nye", "email": "thescienceguy@gmail.com"}
    response = client.post("/user/", json=user)
    assert response.status_code == 422


def test_create_user_invalid_last_name(client, example_user):
    example_user["last_name"] = ""
    response = client.post("/user/", json=example_user)
    assert response.status_code == 422


def test_get_user_by_id(session, client, example_user):
    result = client.post("/user/", json=example_user)
    user_id = result.json()["id"]

    response = client.get(f"/user/{user_id}")
    created_user = response.json()
    assert response.status_code == 200
    assert created_user["first_name"] == example_user["first_name"]
    assert created_user["last_name"] == example_user["last_name"]
    assert created_user["email"] == example_user["email"]


def test_get_user_by_invalid_id(client):
    bad_id = 100
    response = client.get(f"/user/{bad_id}")
    assert response.status_code == 422
    bad_id = uuid.uuid4()
    response = client.get(f"/user/{bad_id}")
    assert response.status_code == 404


def test_update_user(session, client, example_user):
    pass
