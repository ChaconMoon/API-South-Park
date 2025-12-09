"""
Module written by Carlos Chacón.

This module defines the Album data model used to represent South Park music albums
in the API responses. Each Album instance contains information about a specific
South Park album including its ID, name, release date, cover images, songs and URL.
"""

import datetime

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.album_db import AlbumDB


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
    release_date: datetime.date
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

    def __init__(self, album_db: AlbumDB, base_url: str = "") -> "Album":
        """
        Initialize an Album instance from database row data.

        Args:
            album_db (SQL Alchemy Object): Database object containing album data
            base_url (str): Base URL for image paths

        Returns:
            Album: New Album instance

        """
        data = {
            "id": album_db.id,
            "name": album_db.name,
            "release_date": album_db.release_date,
            "album_cover": base_url + album_db.album_cover,
            "web_album_cover": base_url + album_db.web_album_cover,
            "songs": {
                str(index): {
                    "name": song.name,
                    "url": f"{base_url}api/songs/{song.id}",  # noqa: E501
                }
                for index, song in enumerate(album_db.songs)
            },
            "album_url": album_db.album_url,
        }
        super().__init__(**data)
