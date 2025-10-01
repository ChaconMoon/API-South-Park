"""
Module written by Carlos Chacón

This module defines the Album data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Album class
class Album(BaseModel):
    id: int
    name: str
    release_date: str
    album_cover: str
    songs: dict
    album_url: str
