"""
Module written by Carlos Chacón

This module defines the Game data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Game class
class Game(BaseModel):
    id: int
    name: str
    developer: str
    platforms: list[str]
    release_date: str
    images: list[str]
