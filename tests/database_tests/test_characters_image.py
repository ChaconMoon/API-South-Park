"""
Module written by Carlos Chacón.

This Module define the tests if there is a missing file in characters databse.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_image_exist_in_characters():
    """Test all images in Characters database."""
    load_dotenv()
    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Avalible Error")
    total_characters = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_characters_in_database"]
    logging.info(f"\n\nCharacters to test: {total_characters}")

    for i in range(1, total_characters + 1, 1):
        image_urls = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/{i}", timeout=5
        ).json()["images"]
        for url in image_urls:
            logging.info(f"URL to testing {url}")
            if requests.get(str(url), timeout=5).status_code != 200:
                raise requests.RequestException(
                    f"Image of Character Not Found: {i} URL: {url}"
                )
