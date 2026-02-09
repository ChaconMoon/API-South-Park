"""
Module writted by Carlos Chacón.

Define the FortniteCosmetics model.
"""

from typing import Optional

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.fortnite_cosmetics_db import FortniteCosmeticDB


class FortniteCosmetic(BaseModel, ApiObject):
    """
    Represents a Fortnite Cosmetic item.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the cosmetic item
        name (str): Name of the cosmetic item
        type (str): Type/category of the cosmetic item
        rarity (str): Rarity level of the cosmetic item
        price (int): Price of the cosmetic item in V-Bucks
        image (str): URL to the cosmetic item's image
        notes (Optional[str]): Additional notes or description of the cosmetic item

    """

    id: int
    name: str
    type: str
    rarity: str
    price: int
    image: str
    notes: Optional[str] = None

    def toJSON(self, metadata=False, total_results=0):
        """
        Docstring for toJSON.

        :param self: Description
        :param metadata: Description
        :param total_results: Description
        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["fortnite_cosmetic"] = self.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_fortnite_cosmetics_in_database"] = total_results
        return result

    def __init__(
        self, db_object: FortniteCosmeticDB, base_url: str = ""
    ) -> "FortniteCosmetic":
        """
        Initialize a FortniteCosmetic instance from a database object.

        Args:
            db_object (FortniteCosmeticDB): The database object to initialize from
            base_url (str): Base URL for constructing full image URLs
        Returns:
            FortniteCosmetic: Initialized FortniteCosmetic instance

        """
        data = {
            "id": db_object.id,
            "name": db_object.name,
            "type": db_object.type_ref.type,
            "rarity": db_object.rarity_ref.name,
            "price": db_object.price,
            "image": f"{base_url}api/fortnite/cosmetics/{db_object.id}/image",
            "notes": db_object.notes,
        }
        super().__init__(**data)
