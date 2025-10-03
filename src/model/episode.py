"""
Module written by Carlos Chacón

This module defines the Episode data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Episode class
class Episode(BaseModel):
    id: int
    name: str
    episode_numbering: dict
    realese_date: str
    description: str
    episode_in_website: dict
    episode_thumbnail: str
