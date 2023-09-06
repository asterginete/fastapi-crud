from fastapi.testclient import TestClient
from app.main import app
from app.schemas import UserCreate

client = TestClient(app)

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert "id" in data

def test_login():
    user_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/login/", data=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
