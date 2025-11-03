"""
Module written by Carlos Chacón

This module defines the Game data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.controller.data_controller import parse_array_to_list
from src.model.ApiObject import ApiObject


# Create Game class
class Game(BaseModel, ApiObject):
    id: int
    name: str
    developer: str
    platforms: list[str]
    release_date: str
    images: list[str]

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["game"] = self.model_dump()

            # Add Metadata to Response
            result["metadata"] = dict()
            result["metadata"]["total_characters_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url="") -> "Game":
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "developer": str(row[2]) if row[2] is not None else "",
            "platforms": parse_array_to_list(str(row[3])),
            "release_date": str(row[4]) if row[4] is not None else "Not Released",
            "images": parse_array_to_list(str(row[5]), is_url=True, base_url=base_url),
        }
        return super().__init__(**data)
