"""
Module written by Carlos Chacón

This module defines the Alter Ego data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.controller.data_controller import parse_array_to_list
from src.model.ApiObject import ApiObject


# Create Alter Ego class
class AlterEgo(BaseModel, ApiObject):
    id: int
    original_character: str
    name: str
    images: list[str]

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["alterego"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_alteregos_of_this_character_in_database"] = (
                total_results
            )
        return result

    def __init__(self, row: list, base_url: str = "") -> "AlterEgo":
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "original_character": str(row[1]) if row[1] is not None else "",
            "name": str(row[2]) if row[2] is not None else "",
            "images": parse_array_to_list(row[3], is_url=True, base_url=base_url),
        }
        return super().__init__(**data)
