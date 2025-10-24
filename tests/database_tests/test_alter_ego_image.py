import os
import pytest
import requests
from dotenv import load_dotenv


def test_if_image_exist_in_characters():
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
    assert (
        requests.get(f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/").status_code
        == 200
    ), "Database Not Connected"
    for character in list_characters_with_alteregos:
        print(f"Actual Character: {character}")
        actual_character = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/{character}/alteregos"
        ).json()["alteregos"]

        for alter_ego_number in range(0, len(actual_character), 1):
            alter_ego_images = requests.get(
                actual_character[str(alter_ego_number)]["url"]
            ).json()["images"]
            for image in alter_ego_images:
                assert requests.get(image).status_code == 200
