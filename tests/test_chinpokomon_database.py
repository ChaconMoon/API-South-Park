"""
Module written by Carlos Chacón.

This Module define the tests to the responses in chinpokomon databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_chinopokon_database_correct():
    """Test a correct Response in Episode Endpoint."""
    fake_response = {
        "id": 30,
        "name": "Velocirapstar",
        "image": "http://localhost:8000/img/chinpokomon/Velocirapstar.png",
    }
    with patch(
        "src.controller.chinpokomon.chinpokomon_endpoints.get_chinpokomon_by_id"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/api/chinpokomons/1")
        if response.status_code != 200:
            raise ValueError("Expected Found Response")


def test_chinpokomon_object_not_found():
    """Test a not found Response in Episode Endpoint."""
    fake_response = {"error": "Chinpokomon not found", "status": "failed"}
    with patch(
        "src.controller.chinpokomon.chinpokomon_endpoints.get_chinpokomon_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/chinpokomons/1")
        if response.status_code != 404:
            raise ValueError("Expected Not Found Response")


def test_chinpokomon_database_not_avalible():
    """Test a not avalible Response in Episode Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch(
        "src.controller.chinpokomon.chinpokomon_endpoints.get_chinpokomon_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/chinpokomons/1")
        if response.status_code != 500:
            raise ValueError("Expected Internal Server Error Response")
