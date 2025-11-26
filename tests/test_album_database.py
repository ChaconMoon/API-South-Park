"""
Module written by Carlos Chacón.

This Module define the tests to the responses in album databse.
"""

import logging
from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_album_database_correct():
    """Test A Correct Response in Album Endpoint."""
    fake_response = {
        "album": {
            "id": 1,
            "name": "Album Name",
            "release_date": "1998-12-08",
            "album_cover": "http://localhost/image.jpg",
            "songs": {"1": {"name": "song name", "url": "http://localhost/song/1"}},
        },
        "metadata": {"total_albums_in_database": 6},
    }
    with patch(
        "src.controller.music.music_endpoints.get_album_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/albums/1")
        logging.info(response)
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_album_object_not_found():
    """Test A Not Found Response in Album Endpoint."""
    fake_response = {"error": "Album not found", "status": "failed"}
    with patch(
        "src.controller.music.music_endpoints.get_album_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/albums/1")
        logging.info(response)
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_album_database_not_available():
    """Test A Not Available Response in Album Endpoint."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch(
        "src.controller.music.music_endpoints.get_album_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/albums/1")
        logging.info(response.content)
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
