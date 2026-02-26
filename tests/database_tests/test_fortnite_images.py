"""
Module written by Carlos Chacón.

This Module define the tests if there is a missing file in characters databse.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_image_exist_in_fortnite():
    """Test if all Fortnite exists in database."""
    load_dotenv()

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Available Error")

    logging.info("API Available")

    total_cosmetics = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/fortnite/cosmetics/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_fortnite_cosmetics_in_database"]
    logging.info(f"\n\nGames to test: {total_cosmetics}")

    for i in range(1, total_cosmetics + 1, 1):
        logging.info(f"Testing Cosmetic: {i}")

        image_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/fortnite/cosmetics/{i}",
            timeout=5,
        ).json()["image"]
        logging.info(f"URL to testing {image_url}")
        if requests.get(str(image_url), timeout=5).status_code != 200:
            raise requests.RequestException(
                f"Image of Cosmetic Not Found: {i} URL: {image_url}"
            )
