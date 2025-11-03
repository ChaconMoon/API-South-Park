"""
Module written by Carlos Chacón.

This module get the param of the API in the get character operations, make the query to the API and return the result.
"""

from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.game import Game


# Get a Characters by this ID
def get_game_by_id(
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
            text("SELECT * FROM public.games where id = :id"), {"id": id}
        )

        # Return the errors response

        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Game not found", "status": "failed"}
        # Get the Character info
        for row in query_result:
            game = Game(row, base_url)
        result = dict()
        if add_url:
            result["name"] = game.model_dump()["name"]
            result["url"] = f"{base_url}api/games/{row[0]}"
            return result
        # Get the number of characters
        query_result = get_query_result(text("SELECT * FROM public.games"))

        # Return Response
        return game.toJSON(metadata, query_result.rowcount)
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_game_list(ids: list, add_url=False, base_url="") -> dict:
    result = dict()
    result["games"] = dict()
    index = 0

    for character_id in ids:
        result["games"][index] = get_game_by_id(
            character_id, base_url=base_url, metadata=False
        )
        index += 1
    return result
