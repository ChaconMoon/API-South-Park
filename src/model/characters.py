"""
Module written by Carlos Chacón

This module defines the Character data model.
"""

# Import pydantic
from pydantic import BaseModel

# Import List model
from typing import List, Optional


# Create Character class
class Character(BaseModel):
    id: int
    name: str
    friend_group: Optional[int] = None
    family: Optional[int] = None
    birthday: Optional[str] = None
    age: Optional[int] = None
    religion: List[str]
    images: list[str]
    first_apperance: dict
    alter_egos: dict
    famious_guest: bool
