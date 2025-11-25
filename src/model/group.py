"""

Module written by Carlos Chacón.

Defines the Group model and related functions.
"""

from pydantic import BaseModel, ValidationError
from sqlalchemy import text

from src.controller.characters.characters_controller import get_character_by_id
from src.controller.database_connection import get_query_result
from src.model.ApiObject import ApiObject


def get_group_name_by_id(id: int) -> str:
    """
    Retrieve the name of a group from the database by its ID.

    Args:
        id (int): The ID of the group to retrieve.

    Returns:
        str: The name of the group.

    """
    query_execution = get_query_result(
        text(
            """
                SELECT name FROM public.groups
                where "ID" = :id
                """
        ),
        {"id": id},
    )
    query_result = query_execution.mappings().all()
    return str(query_result[0]["name"])


class Group(BaseModel, ApiObject):
    """
    Represents a South Park Group.

    Inherits from:
        BaseModel: Pydantic model for data validation.
        ApiObject: Base interface for API response objects.

    Attributes:
        id (int): The ID of the group.
        name (str): The name of the group.
        known_members (list[dict]): A list of dictionaries representing
        the characters in the group.

    """

    id: int
    name: str
    known_members: list[dict]

    def __init__(self, id: int, rows: list, base_url: str = "") -> "Group":
        """
        Initialize a Group object.

        Args:
            id (int): The ID of the group.
            rows (list): A list of rows from the database containing member IDs.
            base_url (str, optional): The base URL for generating character links.

        Raises:
            ValueError:
            If there is an error building the Group object due to validation issues.

        """
        known_members = []
        try:
            known_members.extend(
                get_character_by_id(int(row[0]), add_url=True, base_url=base_url)
                for row in rows
            )
            data = {
                "id": id,
                "name": get_group_name_by_id(id),
                "known_members": known_members,
            }
            super().__init__(**data)
        except ValidationError as e:
            raise ValueError(f"Error building Group: {str(e)}") from e

    def toJSON(self, metadata=False, total_results=0) -> dict:
        """
        Convert the Group object to a JSON-serializable dictionary.

        Args:
            metadata (bool, optional): Not used in this implementation. Defaults to False.
            total_results (int, optional): Not used in this implementation. Defaults to 0.

        Returns:
            dict: The dictionary representation of the Group object.

        """
        return self.model_dump()
