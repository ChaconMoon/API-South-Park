"""
Module written by Carlos Chacón.

This module defines the music-related endpoints for the South Park API.
It provides routes to access albums and songs from the South Park series.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.music.album_controller import get_album_by_id, get_random_album
from src.controller.music.songs_controller import get_random_song, get_song_by_id

router = APIRouter(tags=["Music"])


@router.get("/api/albums/random")
def show_random_album(
    request: Request, response: Response, exclude_not_available: bool = False
):
    """
    Get a specific South Park album by ID.

    Args:
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        exclude_not_available (boolean): If true excludes the albums not available in streaming srevices

    Returns:
        dict: JSON response containing either:
            - Album data if found
            - Error message if not found or database error

    Response Codes:
        200: Album found and returned successfully
        404: Album not found
        500: Database error

    """  # noqa: E501
    base_url = str(request.base_url)
    json = get_random_album(base_url, exclude_not_available)
    if "error" in json:
        if json["error"] == "Album not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


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
        if json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "album" in json:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/songs/random")
def show_random_song(
    request: Request, response: Response, exclude_not_available: bool = False
):
    """
    Get a specific random song from south park's albums.

    Args:
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        exclude_not_available (boolean): If True excludes the not available songs.

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
    json = get_random_song(exclude_not_available, base_url)
    if "error" in json:
        if json["error"] == "Song not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
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
        elif json["error"] == "Database not available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "song" in json:
        response.status_code = status.HTTP_200_OK
    return json
