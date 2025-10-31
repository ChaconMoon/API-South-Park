"""
Module written by Carlos Chacón

This module defines the Song data model.
"""

# Import pydantic
from pydantic import BaseModel

# Import typing
from typing import Optional

from src.model.ApiObject import ApiObject


# Create song class
class Song(BaseModel, ApiObject):
    id: int
    name: str
    album_number: Optional[int] = None
    lyrics: str
    song_url: str

    def toJSON(self, metadata=False, total_results=0):
        result = dict()
        if not metadata:
            result = self.model_dump()
        else:
            result["song"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_songs_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = ""):
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "album_number": int(row[2]) if row[2] is not None else None,
            "lyrics": str(row[3]) if row[3] is not None else "",
            "song_url": str(row[4]) if row[4] is not None else "",
        }
        return super().__init__(**data)
