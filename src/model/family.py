"""
Module written by Carlos Chacón.

This module defines the Family data model used to represent South Park families
in the API responses. Each Family instance contains information about a specific
South Park family including its ID, name, members and associated images.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.families_db import FamilyDB


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
            return self.model_dump()
        else:
            result = dict()
            result["family"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_families_in_database"] = total_results
        return result

    def __init__(
        self,
        family_db: FamilyDB,
        base_url: str = "",
    ) -> "Family":
        """
        Initialize a Family instance from database rows data.

        Args:
            rows (list): Database rows containing family members data
            family_db (FamilyDB) : The result of the family query
            base_url (str): Base URL for image paths

        Returns:
            Family: New Family instance

        """
        try:
            family_members = [
                {
                    "name": character.name,
                    "url": f"{base_url}api/characters/{character.id}",
                }
                for character in family_db.characters
            ]

            data = {
                "id": family_db.id,
                "name": family_db.name,
                "images": [base_url + x for x in family_db.images],
                "members": family_members,
            }

            return super().__init__(**data)
        except Exception as e:
            raise ValueError(f"Error building Family: {str(e)}") from e
