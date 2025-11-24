"""
Module written by Carlos Chacón.

This Module define the tests to check if the Health Check returns a correct status code.
"""

from unittest.mock import patch

from fastapi.testclient import TestClient
from requests import RequestException

from src.main import app

client = TestClient(app)


def test_database_connection_correct():
    """Test A Correct Response of the Health Check."""
    fake_response = {
        "version": """PostgreSQL 15.14 (Debian 15.14-1.pgdg13+1) on x86_64-pc-linux-gnu,
         compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit""",
        "status": "connected",
    }
    with patch(
        "src.controller.structure.health_check_endpoints.get_database_status"
    ) as databse_status:
        databse_status.return_value = fake_response
        response = client.get("/api")
        if response.status_code != 200:
            raise RequestException("Expected Found Response")


def test_database_connection_error():
    """Test A Error Response of the Health Check."""
    fake_response = {"error": "ERROR", "status": "failed"}
    with patch(
        "src.controller.structure.health_check_endpoints.get_database_status"
    ) as database_status:
        database_status.return_value = fake_response
        response = client.get("/api")
        if response.status_code != 500:
            raise RequestException("Expected Not Available Response")
