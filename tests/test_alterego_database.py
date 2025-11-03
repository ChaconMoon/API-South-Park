"""
Module written by Carlos Chacón.

This Module define the tests to the responses in alter ego databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_alterego_database_correct():
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
    with patch("src.main.get_alter_ego_by_character_and_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/character/1/alteregos/1")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_alterego_object_not_found():
    """Test A Not Found Response in Alter Ego Endpoint."""
    fake_response = {"error": "Alter Ego not found", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alteregos/1")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_alterego_database_not_avalible():
    """Test A Not Avalible Response in Alter Ego Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alteregos/1")
        if response.status_code != 500:
            raise RequestException("Expected Not Avalible Response")


def test_all_alteregos_database_correct():
    """Test a correct response in complete Response in Alter Ego Endpoint."""
    fake_response = {
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
    }
    with patch("src.main.get_all_alteregos_of_a_character") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/character/42/alteregos")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_all_alteregos_object_not_found():
    """Test a not found response in complete Response in Alter Ego Endpoint."""
    fake_response = {"error": "Alter Egos not found", "status": "failed"}
    with patch("src.main.get_all_alteregos_of_a_character") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/42/alteregos")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_all_alteregos_database_not_avalible():
    """Test a not avalible response in complete Response in Alter Ego Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_all_alteregos_of_a_character") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/42/alteregos")
        if response.status_code != 500:
            raise RequestException("Expected Not Avalible Response")
