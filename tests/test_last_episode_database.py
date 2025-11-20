"""
Module written by Carlos Chacón.

This Module define the tests to the responses in episode databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_last_episode_database_correct():
    """Test A Correct Response in Last Episode Endpoint."""
    fake_response = {
        "episode": {
            "id": 200,
            "name": "200",
            "episode_numbering": {"season": 14, "episode": 5},
            "realese_date": "2010-04-14",
            "description": "The town of South Park faces a class action lawsuit as every celebrity they've ever ridiculed is out for revenge.",  # noqa: E501
            "episode_in_website": {
                "status": "CENSORED",
                "website_url": "https://www.southparkstudios.com/episodes/uxg9g7/south-park-200-season-14-ep-5",
            },
        },
        "metadata": {"total_episodes_in_database": 324},
    }
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_last_episode"
    ) as databse_response:
        databse_response.return_value = fake_response
        response = client.get("/api/lastepisode/")
        if response.status_code != 200:
            raise ValueError("Expected Found Response")


def test_last_episode_object_not_found():
    """Test A Not Found Response in Last Episode Endpoint."""
    fake_response = {"error": "Episode not found", "status": "failed"}
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_last_episode"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/lastepisode/")
        if response.status_code != 404:
            raise ValueError("Expected Not Found Response")


def test_last_episode_database_not_available():
    """Test A Not Available Response in Last Episode Endpoint."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch(
        "src.controller.tvshow.tv_show_endpoints.get_last_episode"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/lastepisode/")
        if response.status_code != 500:
            raise ValueError("Expected Internal Server Error Response")
