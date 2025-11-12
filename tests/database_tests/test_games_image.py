"""
Module written by Carlos Chacón.

This Module define the tests if there is a missing file in games database.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_image_exist_in_games():
    """Test all images in Games database."""
    load_dotenv()

    logging.info(f"Request URL: {os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/")

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Avalible Error")

    logging.info("API Avalible")

    total_games = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/games/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_games_in_database"]
    logging.info(f"\n\nGames to test: {total_games}")

    for i in range(1, total_games + 1, 1):
        logging.info(f"Testing Game: {i}")

        image_urls = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/games/{i}", timeout=5
        ).json()["images"]
        for url in image_urls:
            logging.info(f"URL to testing {url}")
            if requests.get(str(url), timeout=5).status_code != 200:
                raise requests.RequestException(
                    f"Image of Game Not Found: {i} URL: {url}"
                )
