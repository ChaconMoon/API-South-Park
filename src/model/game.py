"""
Module written by Carlos Chacón.

This module defines the Game data model used to represent South Park games
in the API responses. Each Game instance contains information about a specific
South Park game including its ID, name, developer, platforms, release date and images.
"""

from pydantic import BaseModel

from src.controller.data_controller import parse_array_to_list
from src.model.ApiObject import ApiObject


class Game(BaseModel, ApiObject):
    """
    Represents a South Park game.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the game
        name (str): Title of the game
        developer (str): Company that developed the game
        platforms (list[str]): List of platforms the game was released on
        release_date (str): Release date of the game
        images (list[str]): List of URLs to game images/screenshots

    """

    id: int
    name: str
    developer: str
    platforms: list[str]
    release_date: str
    images: list[str]

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the Game object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of games in database

        Returns:
            dict: JSON-compatible dictionary with game data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["game"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_characters_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "") -> "Game":
        """
        Initialize a Game instance from database row data.

        Args:
            row (list): Database row containing game data
            base_url (str): Base URL for image paths

        Returns:
            Game: New Game instance

        """
        data = {
            "id": int(row[0]) if row[0] is not None else 0,
            "name": str(row[1]) if row[1] is not None else "",
            "developer": str(row[2]) if row[2] is not None else "",
            "platforms": parse_array_to_list(str(row[3])),
            "release_date": str(row[4]) if row[4] is not None else "Not Released",
            "images": parse_array_to_list(str(row[5]), is_url=True, base_url=base_url),
        }
        return super().__init__(**data)
