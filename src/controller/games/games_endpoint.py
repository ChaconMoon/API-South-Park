"""
Module written by Carlos Chacón.

This module defines the game-related endpoints for the South Park API.
It provides routes to access information about South Park video games.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.games.game_controller import (
    get_game_by_id,
    get_game_list,
    get_game_list_by_search,
    get_random_game,
)

router = APIRouter(tags=["Games"])


@router.get("/api/games")
def show_game_list(
    request: Request, response: Response, limit: int = 0, search: str = ""
) -> dict:
    """
    Get a list of South Park games, with optional search and limit.

    Args:
        request (Request): FastAPI request object containing base URL.
        response (Response): FastAPI response object for status codes.
        limit (int): The maximum number of games to return. If 0, No limit
        search (str): A search term to filter games by name. If empty No search

    Returns:
        dict: JSON response containing the list of games.

    Response Codes:
        200: Games found and returned successfully.
        404: No games found for the given search criteria.
        500: Internal server error.

    """
    if search != "":
        json = get_game_list_by_search(
            search, base_url=str(request.base_url), limit=limit
        )
    else:
        json = get_game_list(base_url=str(request.base_url), limit=limit)
    return json


@router.get("/api/games/random")
def show_random_Game(request: Request, response: Response) -> dict:
    """
    Get a random specific South Park game.

    Args:
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes

    Returns:
        dict: JSON response containing either:
            - Game data if found
            - Error message if not found or database error

    Response Codes:
        200: Game found and returned successfully
        404: Game not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_random_game(base_url)
    if "error" in json:
        if json["error"] == "Game not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "game" in json:
            response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/games/{id}/")
def show_game(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific South Park game by ID.

    Args:
        id (int): The ID of the game to retrieve
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing either:
            - Game data if found
            - Error message if not found or database error

    Response Codes:
        200: Game found and returned successfully
        404: Game not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_game_by_id(id=id, base_url=base_url, metadata=metadata)
    if json is None:
        json = {"error": "Game not found", "status": "failed"}
    if "error" in json:
        if json["error"] == "Game not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "game" in json:
            response.status_code = status.HTTP_200_OK
    return json
