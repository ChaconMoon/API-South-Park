"""
Module written by Carlos Chacón

This module defines the Character data model.
"""

# Import pydantic
from pydantic import BaseModel

# Import List model
from typing import List, Optional

from src.controller.characters.alter_ego_controller import (
    get_all_alteregos_of_a_character,
)
from src.controller.tvshow.episodes_controller import get_episode_by_id
from src.controller.data_controller import parse_array_to_list
from src.model.ApiObject import ApiObject


# Create Character class
class Character(BaseModel, ApiObject):
    id: int
    name: str
    friend_group: Optional[int] = None
    family: Optional[int] = None
    birthday: Optional[str] = None
    age: Optional[int] = None
    religion: Optional[List[str]] = None
    images: list[str]
    first_apperance: dict
    alter_egos: Optional[dict] = None
    famous_guest: bool

    def toJSON(self, metadata=False, total_results=0) -> dict:
        # Create API Response

        # Add Character Data to Response
        if not metadata:
            result = self.model_dump()
        else:
            result["character"] = self.model_dump()

            # Add Metadata to Response
            result["metadata"] = dict()
            result["metadata"]["total_characters_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "", id=0) -> "Character":
        """
        Builder method to create a Character instance from a database row

        Args:
            row (list): Database row with character data
            base_url (str): Base URL for images and links

        Returns:
            Character: New Character instance
        """
        try:
            data = {
                "id": int(row[0]) if row[0] is not None else 0,
                "name": str(row[1]) if row[1] is not None else "",
                "friend_group": int(row[2]) if row[2] is not None else None,
                "family": int(row[3]) if row[3] is not None else None,
                "birthday": str(row[4]) if row[4] is not None else None,
                "age": int(row[5]) if row[5] is not None else None,
                "religion": parse_array_to_list(row[6]),
                "first_apperance": get_episode_by_id(
                    int(row[7]), add_url=True, base_url=base_url
                ),
                "images": parse_array_to_list(row[8], is_url=True, base_url=base_url),
                "alter_egos": get_all_alteregos_of_a_character(
                    int(row[0]), add_url=True, base_url=base_url
                ),
                "famous_guest": bool(row[9]) if row[9] is not None else False,
            }
            return super().__init__(**data)
        except Exception as e:
            raise ValueError(f"Error building Character: {str(e)}")
