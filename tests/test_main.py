import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_calculate_addition():
    """Test the add operation."""
    response = client.post("/calculate", json={"operand1": 5, "operand2": 3, "operation": "add"})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_calculate_subtraction():
    """Test the subtract operation."""
    response = client.post("/calculate", json={"operand1": 5, "operand2": 3, "operation": "subtract"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculate_multiplication():
    """Test the multiply operation."""
    response = client.post("/calculate", json={"operand1": 5, "operand2": 3, "operation": "multiply"})
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_calculate_division():
    """Test the divide operation."""
    response = client.post("/calculate", json={"operand1": 6, "operand2": 3, "operation": "divide"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculate_division_by_zero():
    """Test division by zero error."""
    response = client.post("/calculate", json={"operand1": 5, "operand2": 0, "operation": "divide"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}

def test_calculate_invalid_operation():
    """Test invalid operation error."""
    response = client.post("/calculate", json={"operand1": 5, "operand2": 3, "operation": "modulo"})
    assert response.status_code == 400
    assert "Invalid operation 'modulo'" in response.json()["detail"]
    assert "Supported operations are: add, divide, multiply, subtract" in response.json()["detail"]

def test_calculate_invalid_operand_type():
    """Test request with invalid operand type (string instead of number)."""
    response = client.post("/calculate", json={"operand1": "five", "operand2": 3, "operation": "add"})
    assert response.status_code == 422  # Unprocessable Entity
    # The exact error message from Pydantic can vary, so we check for key parts
    assert "value is not a valid integer" in response.text or "value is not a valid float" in response.text
    assert "operand1" in response.text

def test_calculate_missing_field():
    """Test request with a missing field."""
    response = client.post("/calculate", json={"operand1": 5, "operation": "add"})
    assert response.status_code == 422  # Unprocessable Entity
    assert "field required" in response.text
    assert "operand2" in response.text
