from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_character_database_correct():
    fake_response = {
        "character": {
            "id": 42,
            "name": 'Leopold "Butters" Stotch',
            "friend_group": 0,
            "family": 34,
            "birthday": "September 11th",
            "age": 9,
            "religion": ["Roman Catholic", "Blaintology (Temporarily)"],
            "images": ["http://localhost:8000/img/characters/serie/Butters_Stotch.png"],
            "first_apperance": {
                "name": "Clubhouses",
                "url": "http://localhost:8000/episode/25",
            },
            "alter_egos": {
                "0": {
                    "name": "Astronaut Butters",
                    "url": "http://localhost:8000/character/42/alterego/1",
                },
                "1": {
                    "name": "Deckhand Butters",
                    "url": "http://localhost:8000/character/42/alterego/2",
                },
                "2": {
                    "name": "Choirboy Butters",
                    "url": "http://localhost:8000/character/42/alterego/3",
                },
                "3": {
                    "name": "Paladin Butters",
                    "url": "http://localhost:8000/character/42/alterego/4",
                },
            },
            "famious_guest": False,
        },
        "metadata": {"total_characters_in_database": 277},
    }
    with patch("src.main.get_character_by_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/character/1")
        assert response.status_code == 200


def test_character_object_not_found():
    fake_response = {"error": "Character not found", "status": "failed"}
    with patch("src.main.get_character_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1")
        assert response.status_code == 404


def test_character_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_character_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/character/1")
        assert response.status_code == 500
