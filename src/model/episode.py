"""
Module written by Carlos Chacón.

This module defines the Episode data model used to represent South Park episodes
in the API responses. Each Episode instance contains information about a specific
South Park episode including its ID, name, numbering, release date, description,
website availability and thumbnail image.
"""

import datetime

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.episode_db import EpisodeDB


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
    realese_date: datetime.date  # Note: Typo in field name
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

    def __init__(self, episode_db: EpisodeDB, base_url: str = "") -> "Episode":
        """
        Initialize an Episode instance from database row data.

        Args:
            episode_db: Database object with episode data
            base_url (str): Base URL for thumbnail image paths

        Returns:
            Episode: New Episode instance

        """
        data = {
            "id": episode_db.id,
            "name": episode_db.name,
            "episode_numbering": {
                "season": episode_db.season,
                "episode": episode_db.episode,
            },
            "realese_date": episode_db.release_date,
            "description": episode_db.description,
            "episode_in_website": {
                "status": "EXCLUSIVE ON PARAMOUNT PLUS"
                if episode_db.paramount_plus_exclusive
                else "AVAILABLE ON WEBSITE"
                if not episode_db.censored
                else "CENSORED",
                "website_url": episode_db.website_url,
            },
            "episode_thumbnail": base_url + f"api/episodes/{episode_db.id}/thumbnail",
        }
        return super().__init__(**data)
