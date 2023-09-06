from fastapi.testclient import TestClient
from app.main import app
from app.schemas import OrderCreate

client = TestClient(app)

def test_create_order():
    order_data = {
        "user_id": 1,
        "total_price": 49.99,
        "status": "pending"
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == order_data["user_id"]
    assert data["total_price"] == order_data["total_price"]
    assert data["status"] == order_data["status"]
    assert "id" in data

def test_read_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
