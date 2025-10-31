"""
Module written by Carlos Chacón

This module defines the Album data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.controller.music.songs_controller import get_all_songs_of_a_album
from src.model.ApiObject import ApiObject


# Create Album class
class Album(BaseModel, ApiObject):
    id: int
    name: str
    release_date: str
    album_cover: str
    web_album_cover: str
    songs: dict
    album_url: str

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["album"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_albums_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Album":
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
