"""
Module written by Carlos Chacón

This module defines the Family data model.
"""

# Import pydantic
from pydantic import BaseModel


# Create family class
class Family(BaseModel):
    id: int
    name: str
    images: list[str]
