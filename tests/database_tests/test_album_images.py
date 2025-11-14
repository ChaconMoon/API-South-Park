"""
Module written by Carlos Chacón.

This Module define the tests that check if all albums have thier images.
"""

import logging
import os

import requests
from dotenv import load_dotenv


def test_if_exists_image_in_albums():
    """Test if all the albums have their image."""
    load_dotenv()

    logging.info(f"Request URL: {os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/")

    healh_check_request = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/", timeout=10
    )
    if healh_check_request.status_code != 200:
        raise requests.RequestException("API Not Avalible Error")

    logging.info("API Avalible")

    total_albums = requests.get(
        f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/albums/1?metadata=true",
        timeout=10,
    ).json()["metadata"]["total_albums_in_database"]

    logging.info(f"\n\nAlbums to test: {total_albums}")

    for i in range(1, total_albums + 1, 1):
        logging.info(f"Testing Album: {i}")

        album_cover_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/albums/{i}", timeout=5
        ).json()["album_cover"]

        web_album_cover_url = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/albums/{i}", timeout=5
        ).json()["web_album_cover"]

        logging.info(f"Testing: {album_cover_url}")

        album_cover_request = requests.get(album_cover_url, timeout=5)
        if album_cover_request.status_code != 200:
            raise requests.RequestException(f"Album {i} cover not found")

        logging.info(f"Testing: {web_album_cover_url}")

        album_cover_request = requests.get(web_album_cover_url, timeout=5)
        if album_cover_request.status_code != 200:
            raise requests.RequestException(f"Album {i} web cover not found")
