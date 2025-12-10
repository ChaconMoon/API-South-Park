"""
Module written by Carlos Chacón.

This module handles database operations for retrieving South Park character information.
It provides functions to fetch specific characters by ID, search characters by name,
and retrieve lists of characters.
"""

import logging

from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from src.controller import database_connection
from src.model.characters import Character
from src.model.ORM.alter_ego_db import AlterEgoDB
from src.model.ORM.characters_db import CharacterDB


def get_characters_list(base_url: str = "", limit: int = 0) -> dict:
    """
    Return a list of all characters, ordered by ID.

    Args:
        base_url (str): The base URL for generating resource URLs.
        limit (int): The maximum number of characters to return. 0 means no limit.

    Returns:
        dict: A dictionary containing the list of characters.

    """
    session = database_connection.get_database_session()
    try:
        query_characters = session.query(CharacterDB).order_by(CharacterDB.id)

        if limit > 0:
            characters_list = query_characters.limit(limit).all()
        else:
            characters_list = query_characters.all()

        result = {"characters": {}}
        for index, character_db in enumerate(characters_list):
            character = Character(character_db, base_url)
            result["characters"][index] = character.model_dump()
        return result
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_characters_by_search(
    search_param: str, base_url: str = "", limit: int = 10
) -> dict:
    """
    Search for characters by name using partial matching.

    Args:
        search_param (str): Search string to match against character names
        base_url (str): Base URL for API endpoints
        limit (int): Maximum number of results to return

    Returns:
        dict: JSON response containing either:
            - Dictionary of matching characters if found
            - Error message if no matches or database error

    Response Format:
        Success:
            {
                "characters": {
                    0: {character_data},
                    1: {character_data},
                    ...
                }
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        character_list = (
            session.query(CharacterDB)
            .filter(CharacterDB.name.ilike(f"%{search_param}%"))
            .limit(limit)
            .all()
        )
        result = {"characters": {}}
        for index, character_db in enumerate(character_list):
            character = Character(character_db, base_url)
            result["characters"][index] = character.model_dump()
        session.close()
        if result == {"characters": {}}:
            raise ValueError("Not characters found with this value")
        return result

    except ValueError as e:
        return {"error": str(e), "status": "No characters found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_character_by_id(
    id: int, metadata: bool = False, add_url: bool = False, base_url: str = ""
) -> dict:
    """
    Retrieve a specific character from the database by ID.

    Args:
        id (int): The unique identifier of the character
        metadata (bool): Whether to include metadata in response
        add_url (bool): Whether to include API URLs in response
        base_url (str): Base URL for API endpoints

    Returns:
        dict: JSON response containing either:
            - Character data if found
            - Error message if not found or database error

    Response Format:
        Success with add_url=True:
            {
                "name": str,
                "url": str
            }
        Success with metadata=True:
            {
                "character": {...},
                "metadata": {
                    "total_characters_in_database": int
                }
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        character_db = session.query(CharacterDB).filter(CharacterDB.id == id).first()
        if character_db is None:
            raise TypeError("Not Found a character with this ID")
        character = Character(
            character_db,
            base_url,
        )

        if add_url:
            return {
                "name": character.model_dump()["name"],
                "url": f"{base_url}api/characters/{character.id}",
            }
        character_count = session.query(CharacterDB).count()
        return character.toJSON(metadata, character_count)
    except TypeError as e:
        return {"error": str(e), "status": "Character Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_all_characters_with_alterego(base_url: str = ""):
    """
    Return characters that have at least one alter ego.

    This optimized version uses a JOIN to fetch all relevant characters
    in a single database query.

    Args:
        base_url (str): Optional base URL to prepend to character URLs.

    Returns:
        dict: On success: {"characters_with_alterego": [ ... ]}.
              On error: {"error": str, "status": "failed"}.

    """
    try:
        session = database_connection.get_database_session()

        characters_with_alterego = (
            session.query(CharacterDB)
            .join(AlterEgoDB, CharacterDB.id == AlterEgoDB.original_character)
            .distinct()
            .order_by(CharacterDB.id.asc())
            .all()
        )
        result = {
            "characters_with_alterego": [
                Character(char, base_url).toJSON(compacted=True, base_url=base_url)
                for char in characters_with_alterego
            ]
        }
        if result["characters_with_alterego"] == []:
            raise TypeError("Not values found in Alterego Table")
        session.close()
        return result
    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}


def get_random_character(exclude_famous_guests: bool = False, base_url: str = "") -> dict:
    """
    Get a random character's information.

    Args:
        exclude_famous_guests (bool): If True excludes the famous guest from the search.
        base_url (str): the base url used to create the URL from the API.

    Returns:
        dict: JSON response with character data or error

    """
    try:
        session = database_connection.get_database_session()
        query = session.query(CharacterDB)

        if exclude_famous_guests:
            query = query.filter(CharacterDB.famous_guest.is_(False))

        character_db = query.order_by(func.random()).first()

        if character_db is None:
            return {
                "error": "No character found matching the criteria.",
                "status": "failed",
            }

        character = Character(character_db, base_url)
        return character.toJSON()
    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}
