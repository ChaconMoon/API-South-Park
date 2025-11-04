"""
Module written by Carlos Chacón.

This Module define the tests if there is a missing file in alter ego databse.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_image_exist_in_characters():
    """Test if all images of the alter_egos in database."""
    list_characters_with_alteregos = [
        1,
        2,
        3,
        4,
        5,
        7,
        16,
        17,
        19,
        21,
        24,
        27,
        33,
        39,
        42,
        43,
        52,
        58,
        61,
        65,
        78,
        82,
        95,
        99,
        141,
        151,
        171,
        188,
        194,
        199,
    ]
    load_dotenv()
    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Avalible Error")
    for character in list_characters_with_alteregos:
        logging.info(f"Actual Character: {character}")
        actual_character = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/{character}/alteregos",
            timeout=10,
        ).json()["alteregos"]

        for alter_ego_number in range(0, len(actual_character), 1):
            alter_ego_images = requests.get(
                actual_character[str(alter_ego_number)]["url"], timeout=10
            ).json()["images"]
            for image in alter_ego_images:
                if requests.get(image, timeout=10).status_code != 200:
                    raise requests.RequestException(
                        f"""Character: {character} Image: {alter_ego_number},
                        URL: {image} NOT AVALIBLE """
                    )
