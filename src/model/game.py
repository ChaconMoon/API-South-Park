"""
Module written by Carlos Chacón.

This module defines the Game data model used to represent South Park games
in the API responses. Each Game instance contains information about a specific
South Park game including its ID, name, developer, platforms, release date and images.
"""

import datetime
from typing import Optional

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.games_db import GameDB


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
    release_date: Optional[datetime.date] = None
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
            result["metadata"]["total_games_in_database"] = total_results
        return result

    def __init__(self, game_db: GameDB, base_url: str = "") -> "Game":
        """
        Initialize a Game instance from database row data.

        Args:
            game_db (SQL Achemy ORM object): Object with game data
            base_url (str): Base URL for image paths

        Returns:
            Game: New Game instance

        """
        data = {
            "id": game_db.id,
            "name": game_db.name,
            "developer": game_db.developer,
            "platforms": game_db.platforms,
            "release_date": game_db.release_date,
            "images": [base_url.strip("/") + x for x in game_db.images],
        }
        return super().__init__(**data)
