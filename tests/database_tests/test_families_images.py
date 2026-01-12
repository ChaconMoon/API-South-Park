"""
Module written by Carlos Chacón.

This Module define the tests that check if all families have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_images_exists_in_families():
    """Test if all the families have their images."""
    load_dotenv()
    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Available Error")

    logging.info("API Available")

    total_families = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/families/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_families_in_database"]
    logging.info(f"\n\nFamilies to test: {total_families}")

    for i in range(1, total_families + 1, 1):
        logging.info(f"Testing Family: {i}")

        family_images = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/families/{i}", timeout=5
        ).json()["images"]

        for _family_image in family_images:
            logging.info(f"Testing: {_family_image+"?size=small"}")
            family_image_request = requests.get(_family_image+"?size=small", timeout=5)
        if family_image_request.status_code != 200:
            raise requests.RequestException(f"Family {i} not found")
