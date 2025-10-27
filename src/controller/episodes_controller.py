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
            return {"error": "Database not avalible, try press F5", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}

        for row in query_result:
            # Get Episode info
            episode_info = Episode(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                episode_numbering={
                    "season": int(row[2]) if row[2] is not None else "",
                    "episode": int(row[3]) if row[3] is not None else "",
                },
                realese_date=str(row[4]) if row[4] is not None else "",
                description=str(row[5]) if row[5] is not None else "",
                episode_in_website={
                    "status": "EXCLUSIVE ON PARAMOUNT PLUS"
                    if bool(row[8])
                    else "AVALIBLE ON WEBSITE"
                    if bool(row[7]) is not True
                    else "CENSORED",
                    "website_url": str(row[6]) if row[6] is not None else "",
                },
                episode_thumbnail=base_url + str(row[9]) if row[9] is not None else "",
            )

        # Return the result with the URL
        if add_url:
            result = dict()
            result["name"] = episode_info.model_dump()["name"]
            result["url"] = f"{base_url}api/episodes/{row[0]}"
            return result

        # Return Episode info JSON
        query_result = get_query_result(text("SELECT * FROM public.episodes"))

        result = dict()
        if not metadata:
            result = episode_info.model_dump()
        else:
            result["episode"] = episode_info.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_episodes_in_database"] = query_result.rowcount
        return result

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
