from fastapi import APIRouter, Request, Response, status

from src.controller.music.album_controller import get_album_by_id
from src.controller.music.songs_controller import get_song_by_id

router = APIRouter(tags=["Music"])


# Create the endpoint to get the albums.
@router.get("/api/albums/{id}", tags=["Music"])
def show_album(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the album with a specific id.

    Returns:
    A dict with the response.
    """
    base_url = str(request.base_url)
    json = get_album_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Album not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "album" in json:
        response.status_code == status.HTTP_200_OK
    return json


# Create the endpoint to get the songs.
@router.get("/api/songs/{id}", tags=["Music"])
def show_song(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the song with a specific id.

    Returns:
    A dict with the response
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
