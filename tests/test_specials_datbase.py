"""
Module written by Carlos Chacón.

This Module define the tests to the responses in special databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_specials_database_correct():
    """Test A Correct Response in Special Endpoint."""
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
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_special_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/specials/1")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_specials_object_not_found():
    """Test A Not Found Response in Special Endpoint."""
    fake_response = {"error": "Special not found", "status": "failed"}
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_special_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/specials/1")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_specials_database_not_avalible():
    """Test A Not Avalible Response in Special Endpoint."""
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_special_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/specials/1")
        if response.status_code != 500:
            raise RequestException("Expected Not Avalible Response")
