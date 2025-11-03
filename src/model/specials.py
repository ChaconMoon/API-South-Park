"""
Module written by Carlos Chacón.

This module defines the Special data model used to represent South Park paramount plus
specials in the API responses. Each Special instance contains information about a specific
South Park special episode including its ID, title, release date, description,
external link and poster image.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject


class Special(BaseModel, ApiObject):
    """
    Represents a South Park special episode.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the special
        title (str): Title of the special episode
        release_date (str): Original air date of the special
        description (str): Plot summary or description
        link (str): External reference link
        poster (str): URL to the special's poster image

    """

    id: int
    title: str
    release_date: str
    description: str
    link: str
    poster: str

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Special object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of specials in database

        Returns:
            dict: JSON-compatible dictionary with special data

        """
        if not metadata:
            result = self.model_dump()
        else:
            result["special"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_specials_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Special":
        """
        Initialize a Special instance from database row data.

        Args:
            row (list): Database row containing special data
            base_url (str): Base URL for poster image paths

        Returns:
            Special: New Special instance

        """
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "title": str(row[1]) if row[1] is not None else "",
            "release_date": str(row[2]) if row[2] is not None else "",
            "description": str(row[3]) if row[3] is not None else "",
            "link": str(row[4]) if row[4] is not None else "",
            "poster": f"{base_url}{str(row[5])}" if row[5] is not None else "",
        }
        return super().__init__(**data)
