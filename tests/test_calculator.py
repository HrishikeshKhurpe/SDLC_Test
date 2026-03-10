import pytest
import json
from src.main import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Further test-specific configurations can be done here
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def post_calculate(client, data):
    """
    Helper function to make POST requests to the /calculator/calculate endpoint.
    Reduces boilerplate code in tests.
    """
    response = client.post(
        "/calculator/calculate",
        data=json.dumps(data),
        content_type="application/json",
    )
    return response.status_code, json.loads(response.data)

def test_add(client):
    """Test addition operation."""
    payload = {"operand1": 10, "operand2": 5, "operation": "add"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 200
    assert "result" in data
    assert data["result"] == 15

def test_subtract(client):
    """Test subtraction operation."""
    payload = {"operand1": 10, "operand2": 5, "operation": "subtract"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 200
    assert "result" in data
    assert data["result"] == 5

def test_multiply(client):
    """Test multiplication operation."""
    payload = {"operand1": 10, "operand2": 5, "operation": "multiply"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 200
    assert "result" in data
    assert data["result"] == 50

def test_divide(client):
    """Test division operation."""
    payload = {"operand1": 10, "operand2": 5, "operation": "divide"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 200
    assert "result" in data
    assert data["result"] == 2

def test_divide_by_zero(client):
    """Test division by zero error."""
    payload = {"operand1": 10, "operand2": 0, "operation": "divide"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 400
    assert "error" in data
    assert data["error"] == "Cannot divide by zero"

def test_invalid_operation(client):
    """Test invalid operation error."""
    payload = {"operand1": 10, "operand2": 5, "operation": "power"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 400
    assert "error" in data
    assert data["error"] == "Invalid operation: power"

def test_missing_operand(client):
    """Test missing operand error."""
    payload = {"operand1": 10, "operation": "add"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 400
    assert "error" in data
    assert "Missing required parameters: operand2" in data["error"]

def test_invalid_payload(client):
    """Test invalid JSON payload."""
    response = client.post(
        "/calculator/calculate",
        data="this is not json",
        content_type="application/json",
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
    assert data["error"] == "Invalid JSON payload"

def test_non_numeric_operands(client):
    """Test non-numeric operands."""
    payload = {"operand1": "ten", "operand2": 5, "operation": "add"}
    status_code, data = post_calculate(client, payload)
    assert status_code == 400
    assert "error" in data
    assert data["error"] == "Operands must be numeric"
