"""
Module written by Carlos Chacón.

This Module define the tests that check if all groups have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_images_exists_in_groups():
    """Test if all the groups have their images."""
    load_dotenv()
    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Available Error")

    logging.info("API Available")

    total_groups = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/groups/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_groups_in_database"]
    logging.info(f"\n\nGroups to test: {total_groups}")

    for i in range(1, total_groups + 1, 1):
        logging.info(f"Testing Group: {i}")

        group_image = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/groups/{i}", timeout=5
        ).json()["image"]

        family_image_request = requests.get(group_image, timeout=5)
        if family_image_request.status_code != 200:
            raise requests.RequestException(f"Group {i} not found")
