"""
Module written by Carlos Chacón.

This module define the tests to test if all the EasterEgg are available.

"""

import logging
import os

import requests
from dotenv import load_dotenv

from src.controller.others.easter_egg_controller import EasterEggName


def test_easter_eggs():
    """Test If All Define Eastereggs are Available."""
    load_dotenv()
    values = list(EasterEggName.__members__.values())

    for easteregg in values:
        response = requests.get(
            f"{os.getenv('TESTING_SOUTH_PARK_API_URL')}/api/easteregg/{easteregg.name}",
            timeout=10,
        ).json()
        if "message" in response.keys():
            raise requests.RequestException(
                f"""Easter Egg ( {easteregg.name} ) not available """
            )
        else:
            logging.info(f"EasterEgg ( {easteregg.name} ) is available")
