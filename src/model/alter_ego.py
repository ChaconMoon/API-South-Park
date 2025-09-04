"""
Module written by Carlos Chacón

This module defines the Alter Ego data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Alter Ego class
class AlterEgo(BaseModel):
    id: int
    original_character: str
    name: str
    images: list[str]
