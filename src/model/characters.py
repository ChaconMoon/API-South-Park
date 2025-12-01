"""
Module written by Carlos Chacón.

This module defines the Character data model used to represent South Park characters
in the API responses. Each Character instance contains information about a specific
South Park character including their ID, name, group affiliations, personal details,
appearances, and alternate personas.
"""

# Import List model
from typing import List, Optional

from pydantic import BaseModel, ValidationError
from sqlalchemy import text

from src.controller.characters.alter_ego_controller import (
    get_all_alteregos_of_a_character,
)
from src.controller.data_controller import parse_array_to_list
from src.controller.database_connection import get_query_result
from src.controller.tvshow.episodes_controller import get_episode_by_id
from src.model.ApiObject import ApiObject


def get_compact_family(id: int, base_url: str = "") -> dict:
    """
    Retrieve a compact representation of a family from the database.

    Args:
        id (int): The unique identifier for the family.
        base_url (str): The base URL to construct the API URL for the family.

    Returns:
        dict: A dictionary containing the family's name and URL, or an error
              dictionary if the query fails.

    """
    try:
        # Get the result of the query to the databse.
        query_execution = get_query_result(
            text("""
                SELECT f.name from public.families f
                Where f.id=:id
                """),
            {"id": id},
        )
        query_result = query_execution.mappings().all()
        return {
            "name": str(query_result[0]["name"]),
            "url": f"{base_url}api/families/{id}",
        }
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


# Create Character class
class Character(BaseModel, ApiObject):
    """
    Represents a South Park character.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the character
        name (str): Name of the character
        friend_group (Optional[int]): ID of character's friend group
        family (Optional[int]): ID of character's family
        birthday (Optional[str]): Character's birthday
        age (Optional[int]): Character's age
        religion (Optional[List[str]]): Character's religious affiliations
        images (list[str]): List of URLs to character images
        first_apperance (dict): Details about character's first episode
        alter_egos (Optional[dict]): Character's alternate personas
        famous_guest (bool): Whether character is based on a celebrity

    """

    id: int
    name: str
    friend_group: Optional[int] = None
    family: Optional[dict] = None
    birthday: Optional[str] = None
    age: Optional[int] = None
    religion: Optional[List[str]] = None
    images: list[str]
    first_apperance: dict
    alter_egos: Optional[dict] = None
    famous_guest: bool

    def toJSON(
        self, metadata: bool = False, total_results: int = 0, compacted=False, base_url=""
    ) -> dict:
        """
        Convert the Character object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of characters in database

            If is compacted.

            compacted (bool): Return object compacted.
            base_url (str): Url needed to create the url of the compact object.

        Returns:
            dict: JSON-compatible dictionary with character data

        """
        # Create API Response

        # Add Character Data to Response
        if compacted:
            return {
                "name": self.name,
                "url": f"{base_url}api/characters/{self.id}",
            }
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["character"] = self.model_dump()

            # Add Metadata to Response
            result["metadata"] = dict()
            result["metadata"]["total_characters_in_database"] = total_results
        return result

    def __init__(self, row: list, base_url: str = "", id: int = 0) -> "Character":
        """
        Initialize a Character instance from database row data.

        Args:
            row (list): Database row containing character data
            base_url (str): Base URL for image paths
            id (int): Character identifier (optional)

        Returns:
            Character: New Character instance

        Raises:
            ValueError: If there's an error building the Character object

        """
        try:
            data = {
                "id": int(row[0]) if row[0] is not None else 0,
                "name": str(row[1]) if row[1] is not None else "",
                "family": get_compact_family(int(row[2]), base_url)
                if row[2] is not None
                else None,
                "birthday": str(row[3]) if row[3] is not None else None,
                "age": int(row[4]) if row[4] is not None else None,
                "religion": parse_array_to_list(row[5]),
                "first_apperance": get_episode_by_id(
                    int(row[6]), add_url=True, base_url=base_url
                ),
                "images": parse_array_to_list(row[7], is_url=True, base_url=base_url),
                "alter_egos": get_all_alteregos_of_a_character(
                    int(row[0]), add_url=True, base_url=base_url
                ),
                "famous_guest": bool(row[8]) if row[8] is not None else False,
            }
            return super().__init__(**data)
        except ValidationError as e:
            raise ValueError(f"Error building Character: {str(e)}") from e
