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
    """Test A Correct Response in Random Character Endpoint."""
    fake_response = {
        "character": {
            "id": 42,
            "name": 'Leopold "Butters" Stotch',
            "friend_group": 0,
            "family": 34,
            "birthday": "September 11th",
            "age": 9,
            "religion": ["Roman Catholic", "Blaintology (Temporarily)"],
            "images": ["http://localhost:8000/img/characters/show/Butters_Stotch.png"],
            "first_apperance": {
                "name": "Clubhouses",
                "url": "http://localhost:8000/episode/25",
            },
            "alter_egos": {
                "0": {
                    "name": "Astronaut Butters",
                    "url": "http://localhost:8000/character/42/alteregos/1",
                },
                "1": {
                    "name": "Deckhand Butters",
                    "url": "http://localhost:8000/character/42/alteregos/2",
                },
                "2": {
                    "name": "Choirboy Butters",
                    "url": "http://localhost:8000/character/42/alteregos/3",
                },
                "3": {
                    "name": "Paladin Butters",
                    "url": "http://localhost:8000/character/42/alteregos/4",
                },
            },
            "famous_guest": False,
        },
        "metadata": {"total_characters_in_database": 277},
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_random_character"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("api/characters/random")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_character_object_not_found():
    """Test A Not Found Response in Random Character Endpoint."""
    fake_response = {"error": "Character not found", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_character"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/characters/random")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_character_database_not_available():
    """Test A Not Available Response in Random Character Endpoint."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch(
        "src.controller.characters.characters_endpoints.get_random_character"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("api/characters/random")
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
