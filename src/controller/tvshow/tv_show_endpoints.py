"""
Module written by Carlos Chacón.

This module defines the FastAPI endpoints for TV Show related operations including
episodes and specials. It provides routes to fetch the latest episode, specific episodes,
and special episodes from the South Park API.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.tvshow.episodes_controller import get_episode_by_id, get_last_episode
from src.controller.tvshow.specials_controller import get_special_by_id

router = APIRouter(tags=["TV Show"])


@router.get("/api/lastepisode")
def get_the_last_episode() -> dict:
    """
    Get the most recent episode of South Park.

    Returns:
        dict: JSON response containing the latest episode data

    """
    return get_last_episode()


@router.get("/api/specials/{id}")
def show_special(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific South Park special episode by ID.

    Args:
        id (int): The ID of the special episode to retrieve
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing the special episode data

    Response Codes:
        200: Special found and returned successfully
        404: Special not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_special_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Special not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "special" in json:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/episodes/{id}")
def show_episode(
    id: int, response: Response, request: Request, metadata: bool = False
) -> dict:
    """
    Get a specific South Park episode by ID.

    Args:
        id (int): The ID of the episode to retrieve
        response (Response): FastAPI response object for status codes
        request (Request): FastAPI request object containing base URL
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing the episode data

    Response Codes:
        200: Episode found and returned successfully
        404: Episode not found
        500: Database error

    """
    json = get_episode_by_id(id, base_url=str(request.base_url), metadata=metadata)
    if "error" in json:
        if json["error"] == "Episode not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "episode" in json:
        response.status_code = status.HTTP_200_OK
    return json
