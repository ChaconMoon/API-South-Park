"""
Module written by Carlos Chacón.

This module defines the fortnite controllers for the South Park API.
It provides functions to retrieve Fortnite-related content.
"""

import logging

from src.controller import database_connection
from src.model.fortnite_cosmetics import FortniteCosmetic
from src.model.fortnite_items import FortniteItem
from src.model.ORM.fortnite_cosmetics_db import FortniteCosmeticDB
from src.model.ORM.fortnite_items_db import FortniteItemsDB


def get_fortnite_item(item_id: str, base_url: str) -> dict:
    """
    Retrieve Fortnite item details based on the provided item ID.

    Args:
        item_id (str): Unique identifier for the Fortnite item
        base_url (str): Base URL of the API

    Returns:
        dict: JSON response containing either:
            - Fortnite item details if found
            - Error message if item ID is not recognized
    Response Format:
        Success:
            {
                "id": str,
                "name": str,
                "image": str,
                "effect": str,
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        fortnite_item_db = session.query(FortniteItemsDB).filter(FortniteItemsDB.id == item_id).first()
        if fortnite_item_db is None:
            raise AttributeError("Fortnite Item Not Found")
        fortnite_item = FortniteItem(fortnite_item_db, base_url)
        return fortnite_item.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()

def get_fortnite_cosmetic(cosmetic_id: str, base_url: str) -> dict:
    """
    Retrieve Fortnite cosmetic details based on the provided cosmetic ID.

    Args:
        cosmetic_id (str): Unique identifier for the Fortnite cosmetic
        base_url (str): Base URL of the API

    Returns:
        dict: JSON response containing either:
            - Fortnite cosmetic details if found
            - Error message if cosmetic ID is not recognized
    Response Format:
        Success:
            {
                "id": str,
                "name": str,
                "type": str,
                "rarity": str,
                "price": int,
                "images": dict,
                "notes": str,
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        print(f"Queried Fortnite Cosmetic DB: {cosmetic_id}")
        fortnite_cosmetic_db = session.query(FortniteCosmeticDB).filter(FortniteCosmeticDB.id == cosmetic_id).first()
        if fortnite_cosmetic_db is None:
            raise AttributeError("Fortnite Cosmetic Not Found")
        fortnite_cosmetic = FortniteCosmetic(fortnite_cosmetic_db, base_url)
        return fortnite_cosmetic.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
