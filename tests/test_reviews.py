from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ReviewCreate

client = TestClient(app)

def test_create_review():
    review_data = {
        "user_id": 1,
        "item_id": 1,
        "rating": 4.5,
        "comment": "Great product!"
    }
    response = client.post("/reviews/", json=review_data)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == review_data["user_id"]
    assert data["item_id"] == review_data["item_id"]
    assert data["rating"] == review_data["rating"]
    assert data["comment"] == review_data["comment"]
    assert "id" in data

def test_read_reviews():
    response = client.get(f"/reviews/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
