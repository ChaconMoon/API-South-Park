"""
Module written by Carlos Chacón.

This module handles database operations for retrieving South Park game information.
It provides functions to fetch specific games by ID and lists of games from the database.
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.game import Game


def get_game_by_id(
    id: int,
    metadata: bool = False,
    add_url: bool = False,
    base_url: str = "",
) -> dict:
    """
    Retrieve a specific game from the database by its ID.

    Args:
        id (int): The unique identifier of the game
        metadata (bool): Whether to include metadata in the response
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints

    Returns:
        dict: JSON response containing either:
            - Game data if found
            - Error message if not found or database error

    Response Format:
        Success with add_url=True:
            {
                "name": str,
                "url": str
            }
        Success with metadata=True:
            {
                "game": {...},
                "metadata": {
                    "total_games_in_database": int
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
            text("SELECT * FROM public.games where id = :id"), {"id": id}
        )

        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Game not found", "status": "failed"}

        for row in query_result:
            game = Game(row, base_url)

        if add_url:
            return {
                "name": game.model_dump()["name"],
                "url": f"{base_url}api/games/{row[0]}",
            }

        query_result = get_query_result(text("SELECT * FROM public.games"))
        return game.toJSON(metadata, query_result.rowcount)

    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_game_list(ids: list[int], add_url: bool = False, base_url: str = "") -> dict:
    """
    Retrieve a list of games by their IDs.

    Args:
        ids (list[int]): List of game IDs to retrieve
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints

    Returns:
        dict: JSON response containing:
            {
                "games": {
                    0: {game_data},
                    1: {game_data},
                    ...
                }
            }

    """
    result = {"games": {}}

    for index, game_id in enumerate(ids):
        result["games"][index] = get_game_by_id(
            game_id, base_url=base_url, metadata=False
        )
    return result
