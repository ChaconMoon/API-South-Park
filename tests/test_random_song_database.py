"""
Module written by Carlos Chacón.

This Module define the tests to the responses in song databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_random_song_database_correct():
    """Test a correct Response in Random Episode Endpoint."""
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
    with patch(
        "src.controller.music.music_endpoints.get_random_song"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/api/songs/random")
        if response.status_code != 200:
            raise ValueError("Expected Found Response")


def test_random_song_object_not_found():
    """Test a not found Response in Random Episode Endpoint."""
    fake_response = {"error": "Song not found", "status": "failed"}
    with patch(
        "src.controller.music.music_endpoints.get_random_song"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/songs/random")
        if response.status_code != 404:
            raise ValueError("Expected Not Found Response")


def test_random_song_database_not_avalible():
    """Test a not avalible Response in Random Episode Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch(
        "src.controller.music.music_endpoints.get_random_song"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/songs/random")
        if response.status_code != 500:
            raise ValueError("Expected Internal Server Error Response")
