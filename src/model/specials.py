"""
Module written by Carlos Chacón

This module defines the Special data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.model.ApiObject import ApiObject


# Create Special class
class Special(BaseModel, ApiObject):
    id: int
    title: str
    release_date: str
    description: str
    link: str
    poster: str

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["special"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_specials_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url="") -> "Special":
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "title": str(row[1]) if row[1] is not None else "",
            "release_date": str(row[2]) if row[2] is not None else "",
            "description": str(row[3]) if row[3] is not None else "",
            "link": str(row[4]) if row[4] is not None else "",
            "poster": f"{base_url}{str(row[5])}" if row[5] is not None else "",
        }
        return super().__init__(**data)
