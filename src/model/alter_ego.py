"""
Module written by Carlos Chacón.

This module defines the AlterEgo data model used to represent South Park character
alternate personas in the API responses. Each AlterEgo instance contains information
about a specific alternate persona including its ID, original character, name and images.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.alter_ego_db import AlterEgoDB


class AlterEgo(BaseModel, ApiObject):
    """
    Represents a South Park character's alternate persona.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the alter ego
        original_character (str): Name of the original character
        name (str): Name of the alter ego persona
        images (list[str]): List of URLs to alter ego images

    """

    id: int
    original_character: dict
    name: str
    images: list[str]

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the AlterEgo object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of alter egos for this character

        Returns:
            dict: JSON-compatible dictionary with alter ego data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["alterego"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_alteregos_of_this_character_in_database"] = (
                total_results
            )
        return result

    def __init__(self, alterego_db=AlterEgoDB, base_url: str = "") -> "AlterEgo":
        """
        Initialize an AlterEgo instance from database row data.

        Args:
            alterego_db (AlterEgoDB): The AlterEgo Object from the database.
            base_url (str): Base URL for image paths

        Returns:
            AlterEgo: New AlterEgo instance

        """
        data = {
            "id": alterego_db.id,
            "original_character": {
                "name": alterego_db.character.name,
                "url": f"{base_url}api/characters/{alterego_db.original_character}",
            },
            "name": alterego_db.name,
            "images": [base_url.strip("/") + x for x in alterego_db.images],
        }
        return super().__init__(**data)
