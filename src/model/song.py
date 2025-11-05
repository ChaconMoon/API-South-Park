"""
Module written by Carlos Chacón.

This module defines the Song data model used to represent South Park songs
in the API responses. Each Song instance contains information about a specific
South Park song including its ID, name, album number, lyrics and song URL.
"""

from typing import Optional

from pydantic import BaseModel

from src.model.ApiObject import ApiObject


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

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Song object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of songs in database

        Returns:
            dict: JSON-compatible dictionary with song data

        """
        result = dict()
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["song"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_songs_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Song":
        """
        Initialize a Song instance from database row data.

        Args:
            row (list): Database row containing song data
            base_url (str): Base URL for song URLs (optional)

        Returns:
            Song: New Song instance

        """
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "album_number": int(row[2]) if row[2] is not None else None,
            "lyrics": str(row[3]) if row[3] is not None else "",
            "song_url": str(row[4]) if row[4] is not None else "",
        }
        return super().__init__(**data)
