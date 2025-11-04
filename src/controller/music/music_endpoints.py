"""
Module written by Carlos Chacón.

This module defines the music-related endpoints for the South Park API.
It provides routes to access albums and songs from the South Park series.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.music.album_controller import get_album_by_id
from src.controller.music.songs_controller import get_song_by_id

router = APIRouter(tags=["Music"])


@router.get("/api/albums/{id}")
def show_album(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific South Park album by ID.

    Args:
        id (int): The ID of the album to retrieve
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing either:
            - Album data if found
            - Error message if not found or database error

    Response Codes:
        200: Album found and returned successfully
        404: Album not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_album_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Album not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "album" in json:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/songs/{id}")
def show_song(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific South Park song by ID.

    Args:
        id (int): The ID of the song to retrieve
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing either:
            - Song data if found
            - Error message if not found or database error

    Response Codes:
        200: Song found and returned successfully
        404: Song not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_song_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Song not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "song" in json:
        response.status_code = status.HTTP_200_OK
    return json
