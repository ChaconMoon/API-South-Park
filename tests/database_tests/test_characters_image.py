import os
import pytest
import requests
from dotenv import load_dotenv


def test_if_image_exist_in_characters():
    load_dotenv()
    assert (
        requests.get(f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/").status_code
        == 200
    ), "Database Not Connected"
    total_characters = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/1?metadata=true"
    ).json()["metadata"]["total_characters_in_database"]
    print(f"\n\nCharacters to test: {total_characters}")

    for i in range(1, total_characters + 1, 1):
        image_urls = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/characters/{i}"
        ).json()["images"]
        for url in image_urls:
            print(url)
            assert requests.get(str(url)).status_code == 200, (
                f"Image of Character Not Found: {i}"
            )
