"""
Module written by Carlos Chacón.

This module defines the Song data model used to represent South Park songs
in the API responses. Each Song instance contains information about a specific
South Park song including its ID, name, album number, lyrics and song URL.
"""

from typing import Optional

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.album_songs_db import AlbumSongDB


class Song(BaseModel, ApiObject):
    """
    Represents a South Park song.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the song
        name (str): Title of the song
        album_number (Optional[int]): Album number containing the song, if any
        lyrics (str): Song lyrics text
        song_url (str): URL to listen/download the song

    """

    id: int
    name: str
    album_number: Optional[int] = None
    lyrics: str
    song_url: str

    def toJSON(
        self, metadata: bool = False, total_results: int = 0, compacted=False, base_url=""
    ) -> dict:
        """
        Convert the Song object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response.
            total_results (int): Total number of songs in database.
            compacted (bool): If the json response must be compacted.
            base_url (str): The URL used to create the url in response.

        Returns:
            dict: JSON-compatible dictionary with song data.

        """
        if compacted:
            return {
                "name": self.model_dump()["name"],
                "url": f"{base_url}api/songs/{self.model_dump()['id']}",
            }
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["song"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_songs_in_database"] = total_results
            return result

    def __init__(self, song_db=AlbumSongDB, base_url: str = "") -> "Song":
        """
        Initialize a Song instance from database row data.

        Args:
            song_db (SQLAlchemy Object ORM): Database object with song data
            base_url (str): Base URL for song URLs (optional)

        Returns:
            Song: New Song instance

        """
        data = {
            "id": song_db.id,
            "name": song_db.name,
            "album_number": song_db.album_id,
            "lyrics": song_db.lyrics,
            "song_url": song_db.song_url,
        }
        return super().__init__(**data)
