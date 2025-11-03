"""
Module written by Carlos Chacón.

This module defines the Family data model used to represent South Park families
in the API responses. Each Family instance contains information about a specific
South Park family including its ID, name, members and associated images.
"""

from pydantic import BaseModel

from src.controller.characters.characters_controller import get_character_by_id
from src.controller.data_controller import parse_array_to_list
from src.model.ApiObject import ApiObject


class Family(BaseModel, ApiObject):
    """
    Represents a South Park family.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the family
        name (str): Name of the family
        images (list[str]): List of URLs to family images
        members (list[dict]): List of character dictionaries belonging to the family

    """

    id: int
    name: str
    images: list[str]
    members: list[dict]

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Family object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of families in database

        Returns:
            dict: JSON-compatible dictionary with family data

        """
        if not metadata:
            result = self.model_dump()
        else:
            result["family"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_families_in_database"] = total_results
        return result

    def __init__(self, rows: list, base_url: str = "", id: int = 1) -> "Family":
        """
        Initialize a Family instance from database rows data.

        Args:
            rows (list): Database rows containing family members data
            base_url (str): Base URL for image paths
            id (int): Family identifier

        Returns:
            Family: New Family instance

        """
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
