"""
Module written by Carlos Chacón.

This module defines the Special data model used to represent South Park paramount plus
specials in the API responses. Each Special instance contains information about a specific
South Park special episode including its ID, title, release date, description,
external link and poster image.
"""

import datetime

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.special_db import SpecialDB


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
    release_date: datetime.date
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
            return self.model_dump()
        else:
            result = dict()
            result["special"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_specials_in_database"] = total_results
        return result

    def __init__(self, special_db: SpecialDB, base_url: str = "") -> "Special":
        """
        Initialize a Special instance from database row data.

        Args:
            special_db (Special Databse item): Database object with special data
            base_url (str): Base URL for poster image paths

        Returns:
            Special: New Special instance

        """
        data = {
            "id": special_db.id,
            "title": special_db.title,
            "release_date": special_db.release_date,
            "description": special_db.description,
            "link": special_db.link,
            "poster": base_url + special_db.poster,
        }
        return super().__init__(**data)
