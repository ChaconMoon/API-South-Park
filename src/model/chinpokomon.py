"""
Module written by Carlos Chacón.

This module defines the Chinpokomon data model used to represent South Park Chinpokomon
in the API responses. Each Chinpokomon instance contains information about a specific
Chinpokomon including its ID, name, and associated image.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject


class Chinpokomon(BaseModel, ApiObject):
    """
    Represents a South Park Chinpokomon.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the Chinpokomon
        name (str): Name of the Chinpokomon
        image (str): URL to Chinpokomon image

    """

    id: int
    name: str
    image: str

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Chinpokomon object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of Chinpokomon in database

        Returns:
            dict: JSON-compatible dictionary with Chinpokomon data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["chinpokomon"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_chinpokomons_in_database"] = total_results
            return result

    def __init__(self, row: list, base_url: str = "") -> "Chinpokomon":
        """
        Initialize a Chinpokomon instance from database row data.

        Args:
            row (list): Database row containing Chinpokomon data
            base_url (str): Base URL for image paths

        Returns:
            Chinpokomon: New Chinpokomon instance

        """
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "image": (base_url + str(row[2])) if row[1] is not None else "",
        }
        return super().__init__(**data)
