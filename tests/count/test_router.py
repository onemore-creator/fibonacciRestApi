import pytest
from httpx import AsyncClient

from app.main import app


from fastapi.testclient import TestClient
from app.main import app  # Assuming your FastAPI app instance is named 'app'

client = TestClient(app)

def test_fibonacci_value_for_number():
    response = client.get("/fibonacci/count/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_get_fibonacci_sequence_from_1_to_n():
    response = client.get("/fibonacci/count/from1toN/10")
    assert response.status_code == 200
    assert response.json() == {"items": ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34"]}

def test_add_number_to_blacklist():
    response = client.post("/fibonacci/blacklist/add/5")
    assert response.status_code == 200
    assert response.json() == 1  # Assuming the result of sadd operation is returned

def test_delete_number_from_blacklist():
    response = client.delete("/fibonacci/blacklist/delete/5")
    assert response.status_code == 204

def test_get_numbers_from_blacklist():
    response = client.get("/fibonacci/blacklist/get")
    assert response.status_code == 200
    assert response.json() == {"numbers": []}  # Assuming an empty blacklist initially

# Add more tests as needed
