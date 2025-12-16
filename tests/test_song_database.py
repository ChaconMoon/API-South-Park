"""
Module written by Carlos Chacón.

This Module define the tests to the responses in song databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_song_database_correct():
    """Test a correct Response in Episode Endpoint."""
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
    with patch("src.controller.music.music_endpoints.get_song_by_id") as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/api/songs/2")
        if response.status_code != 200:
            raise ValueError("Expected Found Response")


def test_song_object_not_found():
    """Test a not found Response in Episode Endpoint."""
    fake_response = {"error": "Song not found", "status": "Not Found"}
    with patch(
        "src.controller.music.music_endpoints.get_song_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/songs/2")
        if response.status_code != 404:
            raise ValueError("Expected Not Found Response")


def test_song_database_not_available():
    """Test a not available Response in Episode Endpoint."""
    fake_response = {
        "error": "Database not available",
        "status": "Database Not Available",
    }
    with patch(
        "src.controller.music.music_endpoints.get_song_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/songs/2")
        if response.status_code != 500:
            raise ValueError("Expected Internal Server Error Response")
