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

from src.controller.database_connection import get_query_result
from src.model.ApiObject import ApiObject
from src.model.ORM.characters_db import CharacterDB


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
        family (Optional[int]): ID of character's family
        birthday (Optional[str]): Character's birthday
        age (Optional[int]): Character's age
        religion (Optional[List[str]]): Character's religious affiliations
        images (list[str]): List of URLs to character images
        debut (dict): Details about character's first episode
        alter_egos (Optional[dict]): Character's alternate personas
        famous_guest (bool): Whether character is based on a celebrity

    """

    id: int
    name: str
    family: Optional[dict] = None
    birthday: Optional[str] = None
    age: Optional[int] = None
    religion: Optional[List[str]] = None
    images: list[str]
    debut: dict
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

    def __init__(self, db_character: CharacterDB, base_url="") -> "Character":
        """
        Initialize a Character instance from database row data.

        Args:
            row (list): Database row containing character data
            base_url (str): Base URL for image paths
            id (int): Character identifier (optional)
            db_character: The Character object from the database.

        Returns:
            Character: New Character instance

        Raises:
            ValueError: If there's an error building the Character object

        """
        try:
            data = {
                "id": db_character.id if db_character.id is not None else 0,
                "name": db_character.name if db_character.name is not None else "",
                "family": (
                    {
                        "name": db_character.family.name,
                        "url": f"{base_url}api/families/{db_character.family_id}",
                    }
                    if db_character.family_id is not None
                    else None
                ),
                "birthday": db_character.birthday
                if db_character.birthday is not None
                else None,
                "age": db_character.age if db_character.age is not None else None,
                "religion": db_character.religion,
                "debut": (
                    {
                        "name": db_character.debut.name,
                        "url": f"{base_url}api/episode/{db_character.debut_episode}",
                    }
                ),
                "images": [base_url.strip("/") + x for x in db_character.images],
                "alter_egos": {
                    str(index): {
                        "name": alter_ego.name,
                        "url": f"{base_url}api/characters/{db_character.id}/alteregos/{alter_ego.id}",  # noqa: E501
                    }
                    for index, alter_ego in enumerate(db_character.alteregos)
                }
                if db_character.alteregos
                else None,
                "famous_guest": db_character.famous_guest
                if db_character.famous_guest is not None
                else False,
            }
            return super().__init__(**data)
        except ValidationError as e:
            raise ValueError(f"Error building Character: {str(e)}") from e
