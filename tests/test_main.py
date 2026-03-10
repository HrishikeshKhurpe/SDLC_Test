from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_read_root():
    """Tests the root endpoint for a successful response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_list_tools_success():
    """Tests the /tools endpoint for a successful response."""
    response = client.get("/tools")
    assert response.status_code == 200
    expected_tools = [
        {"name": "Hammer"},
        {"name": "Screwdriver"},
        {"name": "Wrench"}
    ]
    assert response.json() == expected_tools

def test_list_tools_failure():
    """
    Tests the /tools endpoint when the service layer raises an exception.
    """
    with patch("app.services.tool_service.get_tools") as mock_get_tools:
        # Configure the mock to raise a generic Exception
        mock_get_tools.side_effect = Exception("Database connection failed")

        response = client.get("/tools")

        # Assert that the endpoint returns a 500 Internal Server Error
        assert response.status_code == 500
        # Assert the response body contains the expected error detail
        assert response.json() == {"detail": "An internal server error occurred while fetching tools."}
