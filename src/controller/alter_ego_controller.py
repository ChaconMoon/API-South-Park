"""
Module written by Carlos Chacón.

This module get the param of the API in the get alter ego operations, make the query to the API and return the result.
"""

from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.alter_ego import AlterEgo
from src.controller.data_controller import parse_array_to_list


# Get one Alter Ego by the character and id
def get_alter_ego_by_character_and_id(
    id_alter_ego: int, id_character: int, add_url=False, base_url=""
):
    """
    Get one alter ego of the database

    Args:
        id_alter_ego (int): The id of a ater_ego of the character.
        id_character (int): The id of the character of the alter ego.
        add_url (bool): If the response must contain the URL of the API.
        base_url (str): "The URL base of the API.

    Returns:
        The JSON Response

    """
    try:
        # Get Query result
        query_result = get_query_result(
            text("""
                        SELECT alter_ego.id,characters.name,alter_ego.name as alter_ego, alter_ego.images FROM public.alter_ego, public.characters
                        where characters.id = alter_ego.original_character and characters.id = :id_character AND alter_ego.id = :id_alter_ego"""),
            {"id_character": id_character, "id_alter_ego": id_alter_ego},
        )
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Alter Ego not found", "status": "failed"}

        # Get Alter Ego data
        for row in query_result:
            alter_ego = AlterEgo(
                id=int(row[0]) if row[0] is not None else 0,
                original_character=str(row[1]) if row[1] is not None else "",
                name=str(row[2]) if row[2] is not None else "",
                images=parse_array_to_list(row[3], is_url=True, base_url=base_url),
            )

        # Return the result with the URL
        if add_url:
            result = dict()
            result["name"] = alter_ego.model_dump()["name"]
            result["url"] = (
                f"{base_url}api/character/{id_character}/alterego/{id_alter_ego}"
            )
            return result
        # Return Alter_Ego Info
        query_result = get_query_result(
            text("""
                        SELECT * FROM public.alter_ego where original_character = :id_character"""),
            {"id_character": id_character},
        )
        result = dict()
        result["alterego"] = alter_ego.model_dump()
        result["metadata"] = dict()
        result["metadata"]["total_alteregos_of_this_character_in_database"] = (
            query_result.rowcount
        )

        return result
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


# Get all the alter egos of a character
def get_all_alteregos_of_a_character(id_character: int, add_url=False, base_url=""):
    """
    Get one alter ego of the database

    Args:
        id_character (int): The id of the character of the alter ego.
        add_url (bool): If the response must contain the URL of the API.
        base_url (str): "The URL base of the API.

    Returns:
        The JSON Response

    """
    try:
        # Get the result of the query
        query_result = get_query_result(
            text(
                """SELECT * FROM public.alter_ego where original_character = :id_character order by id asc"""
            ),
            {"id_character": id_character},
        )

        # Get number of alteregos
        number_of_alter_egos = query_result.rowcount

        # If the number of alter egos is 0 return a empty object
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return None

        # Return the list of the alter ego
        alter_ego_id = 1
        result = dict()
        result["alteregos"] = dict()
        while alter_ego_id != number_of_alter_egos + 1:
            result["alteregos"][alter_ego_id - 1] = get_alter_ego_by_character_and_id(
                id_alter_ego=alter_ego_id,
                id_character=id_character,
                base_url=base_url,
                add_url=True,
            )
            alter_ego_id += 1
        return result
    # Control exceptions
    except Exception:
        return {"message": "error"}
