"""
Module written by Carlos Chacón.

This module handles the easter egg feature logic for the South Park API.
It provides functionality to process special keywords and return hidden content
based on those inputs.
"""

import logging

from src.controller import database_connection

# from src.controller.characters.characters_controller import get_specific_character_list
from src.controller.others.easter_egg_enums import EasterEggName, EasterEggType
from src.model.characters import Character
from src.model.ORM.characters_db import CharacterDB
from src.model.ORM.episode_db import EpisodeDB


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
    session = database_connection.get_database_session()
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
            result = {"characters": {}}
            easter_egg_characters = (
                session.query(CharacterDB).filter(CharacterDB.id.in_(items)).all()
            )
            for index, character in enumerate(easter_egg_characters):
                result["characters"][index] = Character(character, base_url).toJSON()
            return result
        case EasterEggType.EPISODES:
            result = {"episodes": {}}
            easter_egg_characters = (
                session.query(EpisodeDB).filter(CharacterDB.id.in_(items)).all()
            )
            for index, character in enumerate(easter_egg_characters):
                result["episodes"][index] = Character(character, base_url).toJSON()
        case EasterEggType.CUSTOM:
            pass
    return {"message": "No Easter Egg Found"}
