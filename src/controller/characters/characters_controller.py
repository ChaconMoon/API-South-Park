"""
Module written by Carlos Chacón.

This module handles database operations for retrieving South Park character information.
It provides functions to fetch specific characters by ID, search characters by name,
and retrieve lists of characters.
"""

import logging

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.characters import Character


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
    try:
        query_result = get_query_result(
            text(
                """SELECT * FROM public.characters
                 where name ilike :search_param limit :limit"""
            ),
            {"search_param": f"%{search_param}%", "limit": limit},
        )

        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}

        result = {"characters": {}}
        for index, row in enumerate(query_result):
            character = Character(row, base_url)
            result["characters"][index] = character.model_dump()
        return result

    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}


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
    try:
        query_result = get_query_result(
            text("SELECT * FROM public.characters Where id=:id"), {"id": id}
        )

        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}

        for row in query_result:
            character = Character(row, base_url)

        if add_url:
            return {
                "name": character.model_dump()["name"],
                "url": f"{base_url}api/characters/{row[0]}",
            }

        query_result = get_query_result(text("SELECT * FROM public.characters"))
        return character.toJSON(metadata, query_result.rowcount)

    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_character_list(ids: list[int], add_url: bool = False, base_url: str = "") -> dict:
    """
    Retrieve a list of characters by their IDs.

    Args:
        ids (list[int]): List of character IDs to retrieve
        add_url (bool): Whether to include API URLs in response
        base_url (str): Base URL for API endpoints

    Returns:
        dict: JSON response containing:
            {
                "characters": {
                    0: {character_data},
                    1: {character_data},
                    ...
                }
            }

    """
    result = {"characters": {}}
    for index, character_id in enumerate(ids):
        result["characters"][index] = get_character_by_id(
            character_id, base_url=base_url, metadata=False
        )
    return result


def get_all_characters_with_alterego(base_url: str = ""):
    """
    Return characters that have at least one alter ego.

    Queries the alter_ego table for distinct original_character IDs (ascending)
    and returns each character using get_character_by_id(..., add_url=True).

    Args:
        base_url (str): Optional base URL to prepend to character URLs.

    Returns:
        dict: On success: {"characters_with_alterego": [ ... ]}.
              On error: {"error": str, "status": "failed"} or {"message": "error"}.

    """
    try:
        # Get the result of the query
        query_result = get_query_result(
            text(
                """SELECT original_character FROM public.alter_ego
                    group by original_character
                    ORDER BY original_character ASC"""
            )
        )

        # If the number of alter egos is 0 return a empty object
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Query error. No Alteregos in database", "status": "failed"}
        result = dict()
        result["characters_with_alterego"] = list()

        for _row in query_result:
            result["characters_with_alterego"].append(
                get_character_by_id(int(_row[0]), add_url=True, base_url=base_url)
            )
        return result
    except Exception as e:
        logging.error(e)
        return {"message": "error"}
