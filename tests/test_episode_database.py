from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_episode_database_correct():
    fake_response = {
        "episode": {
            "id": 200,
            "name": "200",
            "episode_numbering": {"season": 14, "episode": 5},
            "realese_date": "2010-04-14",
            "description": "The town of South Park faces a class action lawsuit as every celebrity they've ever ridiculed is out for revenge.",
            "episode_in_website": {
                "status": "CENSORED",
                "website_url": "https://www.southparkstudios.com/episodes/uxg9g7/south-park-200-season-14-ep-5",
            },
        },
        "metadata": {"total_episodes_in_database": 324},
    }
    with patch("src.main.get_episode_by_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/episode/1")
        assert response.status_code == 200


def test_character_object_not_found():
    fake_response = {"error": "Episode not found", "status": "failed"}
    with patch("src.main.get_episode_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/episode/1")
        assert response.status_code == 404


def test_character_database_not_avalible():
    fake_response = {"error": "Database not avalible, try press F5", "status": "failed"}
    with patch("src.main.get_episode_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/episode/1")
        assert response.status_code == 500
