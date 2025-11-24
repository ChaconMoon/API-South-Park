"""
Module written by Carlos Chacón.

This Module define the tests that check if all episodes have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_exists_image_in_episode():
    """Test if all the episodes have their image."""
    load_dotenv()

    logging.info(f"Request URL: {os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/")

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Available Error")

    logging.info("API Available")

    total_episodes = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/episodes/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_episodes_in_database"]

    logging.info(f"\n\nCharacters to test: {total_episodes}")

    for i in range(1, total_episodes + 1, 1):
        logging.info(f"Testing Family: {i}")

        episode_thumbnail_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/episodes/{i}", timeout=5
        ).json()["episode_thumbnail"]

        logging.info(f"Testing: {episode_thumbnail_url}")

        episode_thumbnail_request = requests.get(episode_thumbnail_url, timeout=5)
        if episode_thumbnail_request.status_code != 200:
            raise requests.RequestException(f"Image of episode {i} not found")
