"""
Module wrritten by Carlos Chacón.

This Module define the tests for butters punishments.
"""

import logging
from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)

def test_butters_punishment_correct():
    """Test A Correct Response in Butters Punishments Endpoint."""
    fake_response = {"id":1,
                     "episode":"http://localhost:8000/api/episodes/75",
                     "reason_of_punishment":"Make a stupid face for the school photo."}
    with patch(
        "src.controller.others.miscellaneous_endpoints.get_butters_punishment_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/butterspunishments/1")
        logging.info(response)
        if response.status_code != 200:
            raise RequestException("Expected Found Response")

def test_butters_punishment_not_found():
    """Test A Not Found Response in Butters Punishments Endpoint."""
    fake_response = {"error": "Butters' punishment with ID 90 not found.", "status": "Not Found"}
    with patch(
        "src.controller.others.miscellaneous_endpoints.get_butters_punishment_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/butterspunishments/90")
        logging.info(response)
        if response.status_code != 404:
            raise RequestException("Expected Not Found Response")

def test_butters_punishment_database_not_available():
    """Test A Not Available Response in Butters Punishments Endpoint."""
    fake_response = {
        "error": "An error occurred while retrieving the punishment.",
        "status": "Database Not Available",
    }
    with patch(
        "src.controller.others.miscellaneous_endpoints.get_butters_punishment_by_id"
    ) as database_response:
        database_response.return_value = fake_response
        response = client.get("/api/butterspunishments/1")
        logging.info(response)
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
