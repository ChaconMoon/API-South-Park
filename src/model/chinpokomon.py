"""
Module written by Carlos Chacón

This module defines the Alter Ego data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Alter Ego class
class Chinpokomon(BaseModel):
    id: int
    name: str
    image: str
