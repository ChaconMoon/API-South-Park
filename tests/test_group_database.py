"""
Module written by Carlos Chacón.

This Module define the tests to the responses in group databse.
"""

import logging
from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_group_database_correct():
    """Test A Correct Response in Group Endpoint."""
    fake_response = {
        "group": {
            "id": 1,
            "name": "The Boys",
            "image": "http://localhost:8000/img/groups/The_Boys.png",
            "known_members": [
                {
                    "name": 'Kenneth "Kenny" McCormick',
                    "url": "http://localhost:8000/api/characters/1",
                },
                {
                    "name": "Eric Theodore Cartman",
                    "url": "http://localhost:8000/api/characters/2",
                },
                {
                    "name": "Kyle Broflovski",
                    "url": "http://localhost:8000/api/characters/3",
                },
                {
                    "name": 'Stanley "Stan" Marsh',
                    "url": "http://localhost:8000/api/characters/4",
                },
            ],
        },
        "metadata": {"total_groups_in_database": 96},
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_group_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/groups/1")
        logging.info(response)
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_group_object_not_found():
    """Test A Not Found Response in Group Endpoint."""
    fake_response = {"error": "Group not found", "status": "Not Found"}
    with patch(
        "src.controller.characters.characters_endpoints.get_group_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/groups/1")
        logging.info(response)
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_group_database_not_available():
    """Test A Not Available Response in Group Endpoint."""
    fake_response = {
        "error": "Database not available",
        "status": "Database Not Available",
    }
    with patch(
        "src.controller.characters.characters_endpoints.get_group_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/groups/1")
        logging.info(response.content)
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
