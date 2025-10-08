"""
Module written by Carlos Chacón.

This module get the param of the API in the get character operations, make the query to the API and return the result.
"""

from sqlalchemy import text
from src.controller.alter_ego_controller import get_all_alteregos_of_a_character
from src.controller.episodes_controller import get_episode_by_id
from src.model.characters import Character
from src.controller.data_controller import parse_array_to_list
from src.controller.database_connection import get_query_result


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
            character = Character(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                friend_group=int(row[2]) if row[2] is not None else None,
                family=int(row[3]) if row[3] is not None else None,
                birthday=str(row[4]) if row[4] is not None else None,
                age=int(row[5]) if row[5] is not None else None,
                religion=parse_array_to_list(row[6]),
                first_apperance=get_episode_by_id(
                    int(row[7]), add_url=True, base_url=base_url
                ),
                images=parse_array_to_list(row[8], is_url=True, base_url=base_url),
                alter_egos=get_all_alteregos_of_a_character(
                    id, add_url=True, base_url=base_url
                ),
                famous_guest=bool(row[9]) if row[9] is not None else False,
            )
        result = dict()
        if add_url:
            result["name"] = character.model_dump()["name"]
            result["url"] = f"{base_url}api/character/{row[0]}"
            return result
        # Get the number of characters
        query_result = get_query_result(text("SELECT * FROM public.characters"))

        # Create API Response

        # Add Character Data to Response
        if not metadata:
            result = character.model_dump()
        else:
            result["character"] = character.model_dump()

            # Add Metadata to Response
            result["metadata"] = dict()
            result["metadata"]["total_characters_in_database"] = query_result.rowcount

        # Return Response
        return result
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
