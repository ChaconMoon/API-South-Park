"""
Module written by Carlos Chacón.

This module get the param of the API in the get episode operations, make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Internal Imports
from src.controller.database_connection import get_query_result
from src.model.episode import Episode


# Get one episode of the database
def get_episode_by_id(id: int, add_url=False, base_url="", metadata=False) -> dict:
    """
    Get one episode of the database

    Args:
        id (int): The id of a Episode.
        add_url (bool): If the response must contain the URL of the API
        base_url (str): "The URL base of the API

    Returns:
        The JSON Response

    """
    try:
        # Get One Episode with this ID
        query_result = get_query_result(
            text("SELECT * FROM public.episodes where id=:id"), {"id": id}
        )
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}

        for row in query_result:
            # Get Episode info
            episode = Episode(row, base_url)

        # Return the result with the URL
        if add_url:
            result = dict()
            result["name"] = episode.model_dump()["name"]
            result["url"] = f"{base_url}api/episodes/{row[0]}"
            return result

        # Return Episode info JSON
        query_result = get_query_result(text("SELECT * FROM public.episodes"))

        return episode.toJSON(metadata, query_result.rowcount)

    # Control Exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_last_episode():
    """
    Returns the last episode of the series

    Returns:
        The JSON Response

    """
    query_result = get_query_result(text("SELECT * FROM public.episodes"))

    episode_id = query_result.rowcount

    return get_episode_by_id(episode_id)
