"""
Module written by Carlos Chacón

This module defines the Alter Ego data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.model.ApiObject import ApiObject


# Create Alter Ego class
class Chinpokomon(BaseModel, ApiObject):
    id: int
    name: str
    image: str

    def toJSON(self, metadata=False, total_results=0):
        result = dict()
        if not metadata:
            return self.model_dump()
        else:
            result["chinpokomon"] = self.model_dump()
            # Add Metadata to Response
            result["metadata"] = dict()
            result["metadata"]["total_chinpokomons_in_database"] = total_results

            return result

    def __init__(self, row: list, base_url="") -> "ApiObject":
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "image": (base_url + str(row[2])) if row[1] is not None else "",
        }
        return super().__init__(**data)
