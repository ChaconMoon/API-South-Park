"""
Module written by Carlos Chacón.

This Module define the tests to the responses in character databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_character_database_correct():
    """Test A Correct Response in Character Endpoint."""
    fake_response = {
        "characters_with_alterego": [
            {
                "name": 'Kenneth "Kenny" McCormick',
                "url": "http://localhost:8000/api/characters/1",
            }
        ]
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_all_characters_with_alterego"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("api/characterswithalterego")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_character_object_not_found():
    """Test A Not Found Response in Character Endpoint."""
    fake_response = {"error": "Query error. No Alteregos in database", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_all_characters_with_alterego"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/characterswithalterego")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_character_database_not_available():
    """Test A Not Available Response in Character Endpoint."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_all_characters_with_alterego"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/characterswithalterego")
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
