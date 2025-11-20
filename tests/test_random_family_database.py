"""
Module written by Carlos Chacón.

This Module define the tests to the responses in family databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_family_database_correct():
    """Test A Correct Response in Random Family Endpoint."""
    fake_response = {
        "family": {
            "id": 1,
            "name": "The Family",
            "images": ["http://localhost"],
            "members": {
                0: {
                    "name": "Person",
                    "url": "http://localhost",
                }
            },
        },
        "metadata": {"total_families_in_database": 54},
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_random_family"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/families/random")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_family_object_not_found():
    """Test A Not Found Response in Random Family Endpoint."""
    fake_response = {"error": "Family not found", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_family"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/families/random")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_family_database_not_available():
    """Test A Not Available Response in Random Family Endpoint."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_family"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/families/random")
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
