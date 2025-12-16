"""

Module written by Carlos Chacón.

Defines the Group model and related functions.
"""

from pydantic import BaseModel, ValidationError

from src.model.ApiObject import ApiObject
from src.model.ORM.groups_db import GroupDB


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
    image: str
    known_members: list[dict] | list

    def __init__(self, group_db: GroupDB, base_url: str = "") -> "Group":
        """
        Initialize a Group object.

        Args:
            id (int): The ID of the group.
            group_db (GroupDB): The ORM object from the database.
            base_url (str, optional): The base URL for generating character links.

        Raises:
            ValueError:
            If there is an error building the Group object due to validation issues.

        """
        try:
            # Use a list comprehension to build the list of member dictionaries
            known_members = [
                {
                    "name": character.name,
                    "url": f"{base_url}api/characters/{character.id}",
                }
                for character in group_db.characters
            ]

            if not known_members:
                known_members = ["NO KNOWN MEMBERS"]

            data = {
                "id": group_db.id,
                "name": group_db.name,
                "image": base_url + group_db.image if group_db.image else None,
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
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["group"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_groups_in_database"] = total_results
            return result
