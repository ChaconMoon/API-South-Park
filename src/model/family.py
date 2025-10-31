"""
Module written by Carlos Chacón

This module defines the Family data model.
"""

# Import pydantic
from pydantic import BaseModel

from src.controller.data_controller import parse_array_to_list
from src.controller.characters.characters_controller import get_character_by_id
from src.model.ApiObject import ApiObject


# Create family class
class Family(BaseModel, ApiObject):
    id: int
    name: str
    images: list[str]
    members: list[dict]

    def toJSON(self, metadata=False, total_results=0):
        if not metadata:
            result = self.model_dump()
        else:
            result["family"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_families_in_database"] = total_results
        return result

    def __init__(self, rows: list, base_url: str = "", id=1) -> "Family":
        family_members = []
        for row in rows:
            family_members.append(
                get_character_by_id(int(row[0]), add_url=True, base_url=base_url)
            )

            data = {
                "id": id,
                "name": str(rows[0][2]),
                "images": [
                    f"{base_url}{image_url}"
                    for image_url in parse_array_to_list(rows[0][3])
                ],
                "members": family_members,
            }
        return super().__init__(**data)
