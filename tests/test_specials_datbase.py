from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_specials_database_correct():
    fake_response = {
        "special": {
            "id": 1,
            "title": "Special Name",
            "realease": "1999-01-01",
            "description": "Lorem Ipsum",
            "link": "https://www.paramountplus.com/movies/video/Ga_vaU8r4h3Ax7aJnrCWG9EV8h0uugvO/",
        },
        "metadata": {"total_songs_in_datbase": 7},
    }
    with patch("src.main.get_special_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/special/1")
        assert response.status_code == 200


def test_specials_object_not_found():
    fake_response = {"error": "Special not found", "status": "failed"}
    with patch("src.main.get_special_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/special/1")
        assert response.status_code == 404


def test_specials_database_not_avalible():
    fake_response = {"error": "Database not avalible, try press F5", "status": "failed"}
    with patch("src.main.get_special_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/special/1")
        assert response.status_code == 500
