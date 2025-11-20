"""
Module written by Carlos Chacón.

This Module define the tests to the responses in alter ego databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_random_alterego_database_correct():
    """Test A Correct Response in Alter Ego Endpoint."""
    fake_response = {
        "alterego": {
            "id": 1,
            "original_character": 'Kenneth "Kenny" McCormick',
            "name": "Mysterion",
            "images": [
                "http://localhost:8000/img/alteregos/phone_destroyer/Mysterion_PhoneDestroyer.png",
                "http://localhost:8000/img/alteregos/show/Mysterion.png",
            ],
        },
        "metadata": {"total_alteregos_of_this_character_in_database": 5},
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_random_alterego"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/api/alteregos/random")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_random_alterego_object_not_found():
    """Test A Not Found Response in Alter Ego Endpoint."""
    fake_response = {"error": "Alter Ego not found", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_alterego"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/alteregos/random")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_random_alterego_database_not_avalible():
    """Test A Not Avalible Response in Alter Ego Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_alterego"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/alteregos/random")
        if response.status_code != 500:
            raise RequestException("Expected Not Avalible Response")
