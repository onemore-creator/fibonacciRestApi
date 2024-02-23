import pytest
from httpx import AsyncClient

from app.main import app


from fastapi.testclient import TestClient
from app.main import app  # Assuming your FastAPI app instance is named 'app'

client = TestClient(app)

def test_fibonacci_value_for_number():
    response = client.get("/fibonacci/count/10")
    assert response.status_code == 200
    assert response.json() == {"number": "55"}
