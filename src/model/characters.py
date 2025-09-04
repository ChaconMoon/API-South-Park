"""
Module written by Carlos Chacón

This module defines the Character data model.
"""

# Import pydantic
from pydantic import BaseModel

# Import List model
from typing import List


# Create Character class
class Character(BaseModel):
    id: int
    name: str
    friend_group: int
    family: int
    birthday: str
    age: int
    religion: List[str]
    images: list[str]
    first_apperance: dict
    alter_egos: dict
    famious_guest: bool
