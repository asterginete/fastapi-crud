from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ItemCreate

client = TestClient(app)

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "This is a test item.",
        "price": 9.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]
    assert "id" in data

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
