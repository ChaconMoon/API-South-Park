from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_album_database_correct():
    fake_response = {
        "album": {
            "id": 1,
            "name": "Album Name",
            "release_date": "1998-12-08",
            "album_cover": "http://localhost/image.jpg",
            "songs": {"1": {"name": "song name", "url": "http://localhost/song/1"}},
        }
    }
    with patch("src.main.get_album_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/album/1")
        assert response.status_code == 200


def test_album_object_not_found():
    fake_response = {"error": "Album not found", "status": "failed"}
    with patch("src.main.get_album_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/album/1")
        assert response.status_code == 404


def test_album_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_album_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/album/1")
        assert response.status_code == 500
