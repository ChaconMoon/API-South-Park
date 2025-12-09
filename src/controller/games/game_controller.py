"""
Module written by Carlos Chacón.

This module handles database operations for retrieving South Park game information.
It provides functions to fetch specific games by ID and lists of games from the database.
"""

from sqlalchemy import func

from src.controller import database_connection
from src.model.game import Game
from src.model.ORM.games_db import GameDB


def get_random_game(base_url="") -> dict:
    """
    Get a Random Game from the databse.

    base_url (str): The base URL used to create the url in the response

    Retruns:
    A dict with the response.
    """
    session = database_connection.get_database_session()

    game_db = session.query(GameDB).order_by(func.random()).first()

    game = Game(game_db, base_url)

    return game.toJSON()


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
        session = database_connection.get_database_session()

        game_db = session.query(GameDB).filter(GameDB.id == id).first()
        game = Game(game_db, base_url)

        if add_url:
            return {
                "name": game.model_dump()["name"],
                "url": f"{base_url}api/games/{id}",
            }
        return game.toJSON()

    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_game_list(add_url: bool = False, base_url: str = "", limit: int = 0) -> dict:
    """
    Retrieve a list of games by their IDs.

    Args:
        ids (list[int]): List of game IDs to retrieve
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints
        limit (int): The number of the games returned, if 0 no limit.

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
    session = database_connection.get_database_session()
    game_query = session.query(GameDB).order_by(GameDB.id)
    if limit != 0:
        game_query = game_query.limit(limit)
    game_list = game_query.all()
    result = {"games": {}}

    for index, game_id in enumerate(game_list):
        result["games"][index] = Game(game_id, base_url).toJSON()
    return result


def get_game_list_by_search(search: str = "", base_url: str = "", limit: int = 0) -> dict:
    """
    Search for games by name using a partial, case-insensitive match.

    Args:
        search (str): The search term to match against game names.
        base_url (str): The base URL for generating resource URLs.
        limit (int): The maximum number of games to return. If 0, no limit.

    Returns:
        dict: A dictionary containing the list of matching games.

    """
    session = database_connection.get_database_session()
    game_query = (
        session.query(GameDB).filter(GameDB.name.ilike(f"%{search}%")).order_by(GameDB.id)
    )
    if limit != 0:
        game_query = game_query.limit(limit)
    game_list = game_query.all()
    result = {"games": {}}

    for index, game_id in enumerate(game_list):
        result["games"][index] = Game(game_id, base_url).toJSON()
    return result
