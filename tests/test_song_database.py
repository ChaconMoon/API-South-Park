from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_song_database_correct():
    fake_response = {
        "song": {
            "id": 1,
            "name": "Song name",
            "album_number": 1,
            "lyrics": "lorem ipsum",
            "song_url": "https://music.youtube.com/watch?v=b7uJyw6eXzg&list=OLAK5uy_kjD121b8XN2_RslyLkocpwY0yS6e85W1Y",
        },
        "metadata": {"total_songs_in_database": 85},
    }
    with patch("src.main.get_song_by_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/song/2")
        assert response.status_code == 200


def test_song_object_not_found():
    fake_response = {"error": "Song not found", "status": "failed"}
    with patch("src.main.get_song_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/song/2")
        assert response.status_code == 404


def test_song_database_not_avalible():
    fake_response = {"error": "Database not avalible, try press F5", "status": "failed"}
    with patch("src.main.get_song_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/song/2")
        assert response.status_code == 500
