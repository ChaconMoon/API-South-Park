"""
Module written by Carlos Chacón.

This Module define the tests that check if all specials have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_exists_image_in_episode():
    """Test if all the specials have their image."""
    load_dotenv()

    logging.info(f"Request URL: {os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/")

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Avalible Error")

    logging.info("API Avalible")

    total_specials = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/specials/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_specials_in_database"]

    logging.info(f"\n\nCharacters to test: {total_specials}")

    for i in range(1, total_specials + 1, 1):
        logging.info(f"Testing Special: {i}")

        special_poster_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/specials/{i}", timeout=5
        ).json()["poster"]

        logging.info(f"Testing: {special_poster_url}")

        special_poster_request = requests.get(special_poster_url, timeout=5)
        if special_poster_request.status_code != 200:
            raise requests.RequestException(f"Poster of special {i} not found")
