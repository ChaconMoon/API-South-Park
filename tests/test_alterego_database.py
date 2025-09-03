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
                "http://localhost:8000/img/alteregos/serie/Mysterion.png",
            ],
        },
        "metadata": {"total_alteregos_of_this_character_in_database": 5},
    }
    with patch("src.main.get_alter_ego_by_character_and_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/character/1/alterego/1")
        assert response.status_code == 200


def test_alterego_object_not_found():
    fake_response = {"error": "Alter Ego not found", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alterego/1")
        assert response.status_code == 404


def test_alterego_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_alter_ego_by_character_and_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1/alterego/1")
        assert response.status_code == 500
