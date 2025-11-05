"""
Module written by Carlos Chacón.

This module handles the database operations for retrieving South Park episodes.
It provides functions to fetch specific episodes by ID and get the latest episode
from the database.
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.episode import Episode


def get_episode_by_id(
    id: int, add_url: bool = False, base_url: str = "", metadata: bool = False
) -> dict:
    """
    Retrieve a specific episode from the database by its ID.

    Args:
        id (int): The unique identifier of the episode
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints
        metadata (bool): Whether to include metadata in the response

    Returns:
        dict: JSON response containing either:
            - Episode data if found
            - Error message if not found or database error occurred

    Response Format:
        Success:
            With add_url=True:
                {"name": str, "url": str}
            With add_url=False:
                {episode_data} or {"episode": episode_data, "metadata": {...}}

    Error:
            {"error": str, "status": "failed"}

    """
    try:
        query_result = get_query_result(
            text("SELECT * FROM public.episodes where id=:id"), {"id": id}
        )
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Episode not found", "status": "failed"}

        for row in query_result:
            episode = Episode(row, base_url)

        if add_url:
            return {
                "name": episode.model_dump()["name"],
                "url": f"{base_url}api/episodes/{row[0]}",
            }

        query_result = get_query_result(text("SELECT * FROM public.episodes"))
        return episode.toJSON(metadata, query_result.rowcount)

    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_last_episode() -> dict:
    """
    Retrieve the most recent episode from the database.

    Returns:
        dict: JSON response containing either:
            - Latest episode data if found
            - Error message if database error occurred

    Response Format:
        Success:
            {episode_data}

    Error:
            {"error": str, "status": "failed"}

    """
    query_result = get_query_result(text("SELECT * FROM public.episodes"))
    if query_result is None:
        return {"error": "Database not available", "status": "failed"}
    episode_id = query_result.rowcount
    return get_episode_by_id(episode_id)
