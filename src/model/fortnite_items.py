"""
Module writted by Carlos Chacón.

Define the FortniteCosmeticsRarity table model.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.fortnite_items_db import FortniteItemsDB


class FortniteItem(BaseModel, ApiObject):
    """
    Represents a Fortnite item.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the item
        name (str): Name of the item
        image (str): URL to the item's thumbnail image
        effect (str): Description of the item's effect

    """

    id: int
    name: str
    image: str
    effect: str

    def __init__(self, db_object: FortniteItemsDB, base_url: str = "") -> "FortniteItem":
        """
        Initialize a FortniteItem instance from a database object.

        Args:
            db_object (FortniteItemsDB): The database object to initialize from
            base_url (str): Base URL for constructing full image URLs

        Returns:
            FortniteItem: Initialized FortniteItem instance

        """
        data = {
            "id": db_object.id,
            "name": db_object.name,
            "image": f"{base_url}api/fortnite/item/{db_object.id}/image",
            "effect": db_object.effect,
        }
        super().__init__(**data)

    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the FortniteItem object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of items in database

        Returns:
            dict: JSON-compatible dictionary with item data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["fortnite_item"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_fortnite_items_in_database"] = total_results
        return result
