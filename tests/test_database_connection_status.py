from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_database_connection_correct():
    fake_response = {
        "version": "PostgreSQL 15.14 (Debian 15.14-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit",
        "status": "connected",
    }
    with patch("src.main.get_database_status") as databse_status:
        databse_status.return_value = fake_response
        response = client.get("/")
        assert response.status_code == 200


def test_database_connection_error():
    fake_response = {"error": "ERROR", "status": "failed"}
    with patch("src.main.get_database_status") as database_status:
        database_status.return_value = fake_response
        response = client.get("/")
        assert response.status_code == 500
