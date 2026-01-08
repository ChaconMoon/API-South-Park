"""
Module written by Carlos Chacón.

This module defines the FastAPI endpoints for TV Show related operations including
episodes and specials. It provides routes to fetch the latest episode, specific episodes,
and special episodes from the South Park API.
"""

from fastapi import APIRouter, Query, Request, Response, status
from fastapi.responses import StreamingResponse
from typing_extensions import Annotated

from src.controller.tvshow.episodes_controller import (
    get_episode_by_id,
    get_episode_images_by_id_,
    get_episode_list,
    get_episode_list_by_search,
    get_last_episode,
    get_random_episode,
)
from src.controller.tvshow.specials_controller import (
    get_random_special,
    get_special_by_id,
)

router = APIRouter(tags=["TV Show"])


@router.get("/api/episodes/{epsiode_id}/thumbnail")
def get_episode_image(epsiode_id: int,
    size: Annotated[str, Query(regex="^(original|small|medium|large)$")] = "original"
    ) -> StreamingResponse:
    """
    Get a specific image for a South Park episode by episode ID and image ID.

    Args:
        epsiode_id (int): The ID of the episode.
        id (int): The ID of the image.
        size (str): The desired size of the image
          ("original", "large", "medium", "small").

    Returns:
        StreamingResponse: The image file as a streaming response.

    Response Codes:
        200: Image found and returned successfully.
        404: Image not found.
        500: Internal server error.

    """
    return get_episode_images_by_id_(epsiode_id, id, size)
@router.get("/api/episodes")
def show_episode_list(
    response: Response, request: Request, search: str = "", limit: int = 0
) -> dict:
    """
    Get a list of South Park episodes, with optional search and limit.

    Args:
        response (Response): FastAPI response object for status codes.
        request (Request): FastAPI request object containing base URL.
        search (str): A search term to filter episodes by name (If is not empty).
        limit (int): The maximum number of episodes to return (if is not 0).

    Returns:
        dict: JSON response containing the list of episodes.

    Response Codes:
        200: Episodes found and returned successfully.
        404: No episodes found for the given search criteria.
        500: Internal server error.

    """
    if search != "":
        json = get_episode_list_by_search(search, limit, base_url=str(request.base_url))
    else:
        json = get_episode_list(base_url=str(request.base_url), limit=limit)
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


@router.get("/api/lastepisode")
def get_the_last_episode(response: Response, request: Request) -> dict:
    """
    Get the most recent episode of South Park.

    Returns:
        dict: JSON response containing the latest episode data

    """
    json = get_last_episode(str(request.base_url))
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


@router.get("/api/specials/random")
def show_random_special(request: Request, response: Response):
    """
    Get a random South Park special.

    Args:
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes

    Returns:
        dict: JSON response containing the special episode data

    Response Codes:
        200: Special found and returned successfully
        404: Special not found
        500: Database error

    """
    json = get_random_special(base_url=str(request.base_url))
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


# The Standard Endpoints must be defined before the param endpoints
@router.get("/api/episodes/random")
def show_random_episode(
    request: Request,
    response: Response,
    exclude_paramount_plus: bool = False,
    exclude_censored: bool = False,
):
    """
    Get a random episode.

    Args:
        response (Response): FastAPI response object for status codes.
        request (Request): FastAPI request object containing base URL.
        exclude_paramount_plus (Boolean): If True excludes the Paramount+ episodes.
        exclude_censored (Boolean): If True excludes the censored episodes.

    Returns:
        dict: JSON response containing the episode data

    Response Codes:
        200: Episode found and returned successfully
        404: Episode not found
        500: Database error

    """
    json = get_random_episode(
        exclude_paramount_plus=exclude_paramount_plus,
        exclude_censored=exclude_censored,
        base_url=str(request.base_url),
    )
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json

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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json
