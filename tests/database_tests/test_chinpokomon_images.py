"""
Module written by Carlos Chacón.

This Module define the tests that check if all chinpokomons have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_exists_image_in_chinpokomon():
    """Test if all the chinpokomons have their image."""
    load_dotenv()

    logging.info(f"Request URL: {os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/")

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Available Error")

    logging.info("API Available")

    total_chinpokomons = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/chinpokomons/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_chinpokomons_in_database"]

    logging.info(f"\n\nCharacters to test: {total_chinpokomons}")

    for i in range(1, total_chinpokomons + 1, 1):
        logging.info(f"Testing Family: {i}")

        chinpokomon_iamge_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/chinpokomons/{i}", timeout=5
        ).json()["image"]

        logging.info(f"Testing: {chinpokomon_iamge_url}")

        chinpokomon_iamge_request = requests.get(chinpokomon_iamge_url, timeout=5)
        if chinpokomon_iamge_request.status_code != 200:
            raise requests.RequestException(f"Image of chinpokomon {i} not found")
