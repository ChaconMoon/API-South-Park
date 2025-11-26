"""
Module written by Carlos Chacón.

This module handles the easter egg feature logic for the South Park API.
It provides functionality to process special keywords and return hidden content
based on those inputs.
"""

import logging
from enum import Enum

from src.controller.characters.characters_controller import get_character_list


class EasterEggType(Enum):
    """
    Enumeration of possible easter egg response types.

    Values:
        NONE (0): No easter egg found
        CHARACTERS (1): Return character-based easter egg
        EPISODES (2): Return episode-based easter egg
        CUSTOM (3): Return custom json response easter egg

    """

    NONE = 0
    CHARACTERS = 1
    EPISODES = 2
    CUSTOM = 3


class EasterEggName(Enum):
    """
    Enumeration of the available easteregg with their ID.

    Values:
        IHAVEDIABETES (0): Returns the two kids of the school that have diabetes:
        (Scott Malkinson and Sophie Gray)

        THEWHITEHOUSE (1): Returns all the characters that are
        in the White House at the moment
    """

    IHAVEDIABETES = 0
    THEWHITEHOUSE = 1
    # OTHER = 2


def get_easter_egg(name: str, base_url: str) -> dict:
    """
    Process a keyword and return corresponding easter egg content.

    Args:
        name (str): Keyword to trigger specific easter egg content
        base_url (str): Base URL for API endpoints

    Returns:
        dict: JSON response containing either:
            - Easter egg content based on type
            - Default message if no match found

    Response Format:
        Character Type:
            Returns character list response
        Episode Type:
            Returns episode list response
        Custom Type:
            Returns custom message
        No Match:
            {"message": "No Easter Egg Found"}

    Example Keywords:
        "ihavediabetes": Returns characters 141 and 107

    """
    items = list()
    type = EasterEggType.NONE
    match name.upper():
        case EasterEggName.IHAVEDIABETES.name:
            items = [141, 107]
            type = EasterEggType.CHARACTERS
        case EasterEggName.THEWHITEHOUSE.name:
            items = [616, 617, 412, 657, 193]
            type = EasterEggType.CHARACTERS

    logging.info(items)
    logging.info(type.value)
    match type:
        case EasterEggType.CHARACTERS:
            return get_character_list(ids=items, base_url=base_url)
        case EasterEggType.EPISODES:
            pass
        case EasterEggType.CUSTOM:
            pass
    return {"message": "No Easter Egg Found"}
