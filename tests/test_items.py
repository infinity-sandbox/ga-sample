from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "API is running ✅"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_create_item():
    payload = {"name": "Laptop", "description": "A laptop", "price": 999.99}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] == True
    assert response.json()["data"]["name"] == "Laptop"

def test_get_item():
    # Create first
    client.post("/items/", json={"name": "Phone", "price": 499.99})
    response = client.get("/items/1")
    assert response.status_code == 200

def test_delete_item():
    client.post("/items/", json={"name": "Tablet", "price": 299.99})
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["success"] == True