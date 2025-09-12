from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)


def test_family_database_correct():
    fake_response = {
        "family": {
            "id": 1,
            "name": "The Family",
            "images": ["http://localhost"],
            "members": {
                0: {
                    "name": "Person",
                    "url": "http://localhost",
                }
            },
        },
        "metadata": {"total_families_in_database": 54},
    }
    with patch("src.main.get_family_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/family/1")
        assert response.status_code == 200


def test_family_object_not_found():
    fake_response = {"error": "Family not found", "status": "failed"}
    with patch("src.main.get_family_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/family/1")
        assert response.status_code == 404


def test_family_database_not_avalible():
    fake_response = {"error": "Database not avalible", "status": "failed"}
    with patch("src.main.get_family_by_id") as database_response:
        database_response.return_value = fake_response
        response = client.get("/family/1")
        assert response.status_code == 500
