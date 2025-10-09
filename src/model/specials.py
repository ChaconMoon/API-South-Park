"""
Module written by Carlos Chacón

This module defines the Special data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create Special class
class Special(BaseModel):
    id: int
    title: str
    release_date: str
    description: str
    link: str
    poster: str
