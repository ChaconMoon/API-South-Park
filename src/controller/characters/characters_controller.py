"""
Module written by Carlos Chacón.

This module get the param of the API in the get character operations, make the query to the API and return the result.
"""

from sqlalchemy import text
from src.model.characters import Character
from src.controller.database_connection import get_query_result


def get_characters_by_search(
    search_param: str,
    base_url="",
    limit=10,
) -> dict:
    try:
        # Get one character from the database using this ID
        query_result = get_query_result(
            text(
                "SELECT * FROM public.characters where name ilike :search_param limit :limit"
            ),
            {"search_param": f"%{search_param}%", "limit": limit},
        )
        # Return the errors response

        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}

        result = dict()
        index = 0
        result["characters"] = dict()
        for row in query_result:
            character = Character(row, base_url)
            result["characters"][index] = character.model_dump()
            index += 1
        return result

    except Exception as e:
        print(e)
        return None


# Get a Characters by this ID
def get_character_by_id(
    id: int,
    metadata=False,
    add_url=False,
    base_url="",
) -> dict:
    """
    Get one character of the database

    Args:
        id (int): The id of a Character.
        add_url (bool): If the response must contain the URL of the API
        base_url (str): "The URL base of the API

    Returns:
        The JSON Response

    """
    try:
        # Get one character from the database using this ID
        query_result = get_query_result(
            text("SELECT * FROM public.characters Where id=:id"), {"id": id}
        )

        # Return the errors response

        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}
        # Get the Character info
        for row in query_result:
            character = Character(row, base_url)
            print(character)
        result = dict()
        if add_url:
            result["name"] = character.model_dump()["name"]
            result["url"] = f"{base_url}api/characters/{row[0]}"
            return result
        # Get the number of characters
        query_result = get_query_result(text("SELECT * FROM public.characters"))

        # Return Response
        return character.toJSON(metadata, query_result.rowcount)
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_character_list(ids: list, add_url=False, base_url="") -> dict:
    result = dict()
    result["characters"] = dict()
    index = 0

    for character_id in ids:
        result["characters"][index] = get_character_by_id(
            character_id, base_url=base_url, metadata=False
        )
        index += 1
    return result
