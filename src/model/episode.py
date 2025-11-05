"""
Module written by Carlos Chacón.

This module defines the Episode data model used to represent South Park episodes
in the API responses. Each Episode instance contains information about a specific
South Park episode including its ID, name, numbering, release date, description,
website availability and thumbnail image.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject


class Episode(BaseModel, ApiObject):
    """
    Represents a South Park episode.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the episode
        name (str): Title of the episode
        episode_numbering (dict): Season and episode numbers
        realese_date (str): Original air date of the episode
        description (str): Plot summary or description
        episode_in_website (dict): Website availability status and URL
        episode_thumbnail (str): URL to episode thumbnail image

    """

    id: int
    name: str
    episode_numbering: dict
    realese_date: str  # Note: Typo in field name
    description: str
    episode_in_website: dict
    episode_thumbnail: str

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Episode object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of episodes in database

        Returns:
            dict: JSON-compatible dictionary with episode data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["episode"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_episodes_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Episode":
        """
        Initialize an Episode instance from database row data.

        Args:
            row (list): Database row containing episode data
            base_url (str): Base URL for thumbnail image paths

        Returns:
            Episode: New Episode instance

        """
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
