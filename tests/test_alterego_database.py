from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_alterego_database_correct():
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
        assert response.status_code == 200


def test_alterego_object_not_found():
    fake_response = {"error": "Alter Ego not found", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alteregos/1")
        assert response.status_code == 404


def test_alterego_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alteregos/1")
        assert response.status_code == 500


def test_all_alteregos_database_correct():
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
        assert response.status_code == 200


def test_all_alteregos_object_not_found():
    fake_response = {"error": "Alter Egos not found", "status": "failed"}
    with patch("src.main.get_all_alteregos_of_a_character") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/42/alteregos")
        assert response.status_code == 404


def test_all_alteregos_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_all_alteregos_of_a_character") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/42/alteregos")
        assert response.status_code == 500
