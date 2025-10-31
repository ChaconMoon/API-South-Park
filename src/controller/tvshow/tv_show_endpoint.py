from src.controller.tvshow.episodes_controller import (
    get_episode_by_id,
    get_last_episode,
)
from fastapi import APIRouter, Request, Response, status

from src.controller.tvshow.specials_controller import get_special_by_id

router = APIRouter(tags=["Tv Show"])


@router.get("/api/lastepisode", tags=["TV Show"])
def get_the_last_episode():
    """
    Returns the last episode of the serie.

    Returns:
    A dict with the response
    """
    return get_last_episode()


# Create the endpoint to get the special episodes.
@router.get("/api/specials/{id}", tags=["TV Show"])
def show_special(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the special with a specific id.

    Returns:
    A dict with the response
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


# Create the endpoint to get the episodes.
@router.get("/api/episodes/{id}", tags=["TV Show"])
def show_episode(
    id: int, response: Response, request: Request, metadata: bool = False
) -> dict:
    """
    Get the response with the episode with a specific id.

    Returns:
    A dict with the response
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
