"""
Module Writter by Carlos Chacón.

This module define the test for the game databse.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_game_database_correct():
    """Test a correct response in Game Endpont."""
    fake_response = {
        "id": 28,
        "name": "South Park Pinball (Re-realese)",
        "developer": "Zen Studios",
        "platforms": ["PC", "PS4", "XOne", "PS5", "XSeries", "Switch"],
        "release_date": "2023-10-12",
        "images": ["http://localhost:8000/img/games/South_Park_pinball_Videogames.avif"],
    }
    with patch("src.controller.games.games_endpoint.get_game_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("api/games/28")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_game_database_not_found():
    """Test a not found response in Game Endpont."""
    fake_response = {"error": "Game not found", "status": "failed"}
    with patch("src.controller.games.games_endpoint.get_game_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("api/games/28")
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")


def test_game_database_not_available():
    """Test a not available response in Game Endpont."""
    fake_response = {"error": "Database not available", "status": "failed"}
    with patch("src.controller.games.games_endpoint.get_game_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("api/games/28")
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
