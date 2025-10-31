"""
Module written by Carlos Chacón

This module defines the Episode data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.model.ApiObject import ApiObject


# Create Episode class
class Episode(BaseModel, ApiObject):
    id: int
    name: str
    episode_numbering: dict
    realese_date: str
    description: str
    episode_in_website: dict
    episode_thumbnail: str

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["episode"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_episodes_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Episode":
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "episode_numbering": {
                "season": int(row[2]) if row[2] is not None else "",
                "episode": int(row[3]) if row[3] is not None else "",
            },
            "realese_date": str(row[4]) if row[4] is not None else "",
            "description": str(row[5]) if row[5] is not None else "",
            "episode_in_website": {
                "status": "EXCLUSIVE ON PARAMOUNT PLUS"
                if bool(row[8])
                else "AVALIBLE ON WEBSITE"
                if bool(row[7]) is not True
                else "CENSORED",
                "website_url": str(row[6]) if row[6] is not None else "",
            },
            "episode_thumbnail": base_url + str(row[9]) if row[9] is not None else "",
        }
        return super().__init__(**data)
