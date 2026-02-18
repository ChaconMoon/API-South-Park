"""
Module written by Carlos Chacón.

This module defines the fortnite controllers for the South Park API.
It provides functions to retrieve Fortnite-related content.
"""

import io
import logging

from fastapi.responses import StreamingResponse
from PIL import Image

from src.controller import database_connection
from src.model.fortnite_cosmetics import FortniteCosmetic
from src.model.fortnite_items import FortniteItem
from src.model.ORM.fortnite_cosmetics_db import FortniteCosmeticDB
from src.model.ORM.fortnite_items_db import FortniteItemsDB


def get_fortnite_item_image_by_id(item_id: int, image_size: str) -> StreamingResponse:
    """
    Docstring for get_fortnite_cosmetic_item_by_id.

    :param item_id: Description
    :type item_id: int
    :param image_size: Description
    :type image_size: str
    :return: Description
    :rtype: StreamingResponse
    """
    sizes = {"large": 0.7, "medium": 0.5, "small": 0.3}
    session = database_connection.get_database_session()

    try:
        fortnite_item_db = (
            session.query(FortniteItemsDB).filter(FortniteItemsDB.id == item_id).first()
        )
        item_image = Image.open("./" + fortnite_item_db.image)
        session.close()
        if image_size != "original":
            item_image.thumbnail(
                size=[
                    item_image.width * sizes[image_size],
                    item_image.height * sizes[image_size],
                ]
            )
        buffer = io.BytesIO()
        item_image.save(buffer, format="WEBP")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/webp", status_code=200)
    except AttributeError:
        return StreamingResponse(
            io.BytesIO(b"Item Not Found"),
            media_type="text/plain",
            status_code=404,
        )


def get_fortnite_cosmetic_image_by_id(
    cosmetic_id: str, image_size: str
) -> StreamingResponse:
    """
    Docstring for get_fortnite_cosmetic_image_by_id.

    :param cosmetic_id: Description
    :type cosmetic_id: int
    :param image_size: Description
    :type image_size: str
    :return: Description
    :rtype: StreamingResponse
    """
    sizes = {"large": 0.7, "medium": 0.5, "small": 0.3}
    session = database_connection.get_database_session()
    try:
        cosmetic_image_db = (
            session.query(FortniteCosmeticDB)
            .filter(FortniteCosmeticDB.id == cosmetic_id)
            .first()
        )
        cosmetic_image = Image.open("./" + cosmetic_image_db.images[0])
        session.close()
        if image_size != "original":
            cosmetic_image.thumbnail(
                size=[
                    cosmetic_image.width * sizes[image_size],
                    cosmetic_image.height * sizes[image_size],
                ]
            )
        buffer = io.BytesIO()
        cosmetic_image.save(buffer, format="WEBP")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/webp", status_code=200)
    except AttributeError:
        return StreamingResponse(
            io.BytesIO(b"Cosmetic Not Found"),
            media_type="text/plain",
            status_code=404,
        )


def get_fortnite_item(item_id: str, base_url: str, metadata: bool) -> dict:
    """
    Retrieve Fortnite item details based on the provided item ID.

    Args:
        item_id (str): Unique identifier for the Fortnite item
        base_url (str): Base URL of the API
        metadata (bool): If the response must return metadata

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
        fortnite_item_db = (
            session.query(FortniteItemsDB).filter(FortniteItemsDB.id == item_id).first()
        )
        if fortnite_item_db is None:
            raise AttributeError("Fortnite Item Not Found")
        fortnite_item = FortniteItem(fortnite_item_db, base_url)
        if metadata:
            item_count = session.query(FortniteItemsDB).count()
            return fortnite_item.toJSON(metadata=metadata, total_results=item_count)
        return fortnite_item.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_fortnite_cosmetic(cosmetic_id: str, base_url: str, metadata: bool) -> dict:
    """
    Retrieve Fortnite cosmetic details based on the provided cosmetic ID.

    Args:
        cosmetic_id (str): Unique identifier for the Fortnite cosmetic
        base_url (str): Base URL of the API
        metadata (bool): If the response must return metadata

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
        logging.info(f"Queried Fortnite Cosmetic DB: {cosmetic_id}")
        fortnite_cosmetic_db = (
            session.query(FortniteCosmeticDB)
            .filter(FortniteCosmeticDB.id == cosmetic_id)
            .first()
        )
        if fortnite_cosmetic_db is None:
            raise AttributeError("Fortnite Cosmetic Not Found")
        fortnite_cosmetic = FortniteCosmetic(fortnite_cosmetic_db, base_url)
        if metadata:
            cosmetic_count = session.query(FortniteCosmeticDB).count()
            return fortnite_cosmetic.toJSON(
                metadata=metadata, total_results=cosmetic_count
            )
        return fortnite_cosmetic.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
