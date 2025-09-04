"""
Module written by Carlos Chacón

This module defines the Song data model.
"""

# Import pydantic
from pydantic import BaseModel

# Import typing
from typing import Optional


# Create song class
class Song(BaseModel):
    id: int
    name: str
    album_number: Optional[int] = None
    lyrics: str
    song_url: str
