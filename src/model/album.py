"""
Module written by Carlos Chacón.

This module defines the Album data model used to represent South Park music albums
in the API responses. Each Album instance contains information about a specific
South Park album including its ID, name, release date, cover images, songs and URL.
"""

from pydantic import BaseModel

from src.controller.music.songs_controller import get_all_songs_of_a_album
from src.model.ApiObject import ApiObject


class Album(BaseModel, ApiObject):
    """
    Represents a South Park music album.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the album
        name (str): Name of the album
        release_date (str): Release date of the album
        album_cover (str): URL to album cover image
        web_album_cover (str): URL to web-optimized album cover
        songs (dict): Dictionary of songs in the album
        album_url (str): External URL to album page

    """

    id: int
    name: str
    release_date: str
    album_cover: str
    web_album_cover: str
    songs: dict
    album_url: str

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Album object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of albums in database

        Returns:
            dict: JSON-compatible dictionary with album data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["album"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_albums_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Album":
        """
        Initialize an Album instance from database row data.

        Args:
            row (list): Database row containing album data
            base_url (str): Base URL for image paths

        Returns:
            Album: New Album instance

        """
        cover_url = str(row[3]) if row[3] is not None else ""
        web_cover_url = str(row[5]) if row[5] is not None else ""
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "release_date": str(row[2]) if row[2] is not None else None,
            "album_cover": base_url + cover_url,
            "web_album_cover": base_url + web_cover_url,
            "songs": get_all_songs_of_a_album(int(row[0]), base_url, add_url=True),
            "album_url": str(row[4]) if row[4] is not None else "",
        }
        super().__init__(**data)
