import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_suite():
    """Single test function that runs multiple scenarios (integrated test suite)."""
    # 1. Root and Health Checks
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to FastAPI" in response.text

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

    # 2. Items with Path and Query logic
    # Success scenario (no query)
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "description": "No query provided"}

    # Success scenario (with query)
    response = client.get("/items/42?q=hello")
    assert response.status_code == 200
    assert response.json()["query"] == "hello"

    # Error scenario (negative ID)
    response = client.get("/items/-5")
    assert response.status_code == 400
    assert response.json()["detail"] == "Item ID must be positive"

    # 3. Calculator with Branching (Operations)
    # Test Addition
    response = client.get("/calculate?op=add&x=10&y=5")
    assert response.status_code == 200
    assert response.json()["result"] == 15.0

    # Test Subtraction
    response = client.get("/calculate?op=sub&x=10&y=5")
    assert response.status_code == 200
    assert response.json()["result"] == 5.0

    # Test Multiplication
    response = client.get("/calculate?op=mul&x=10&y=5")
    assert response.status_code == 200
    assert response.json()["result"] == 50.0

    # Test Division (Success)
    response = client.get("/calculate?op=div&x=10&y=5")
    assert response.status_code == 200
    assert response.json()["result"] == 2.0

    # Test Division (Error - zero)
    response = client.get("/calculate?op=div&x=10&y=0")
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]

    # Test Invalid Operation
    response = client.get("/calculate?op=modulo&x=10&y=5")
    assert response.status_code == 400
    assert "Invalid operation" in response.json()["detail"]


if __name__ == "__main__":
    # If run as a script, we can call the test suite directly
    pytest.main([__file__])
