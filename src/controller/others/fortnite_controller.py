"""
Module written by Carlos Chacón.

This module defines the fortnite controllers for the South Park API.
It provides functions to retrieve Fortnite-related content.
"""

import io
import logging

from fastapi.responses import StreamingResponse
from PIL import Image
from sqlalchemy.exc import OperationalError

from src.controller import database_connection
from src.model.fortnite_cosmetics import FortniteCosmetic
from src.model.fortnite_items import FortniteItem
from src.model.ORM.fortnite_cosmetic_types_db import FortniteCosmeticTypesDB
from src.model.ORM.fortnite_cosmetics_db import FortniteCosmeticDB
from src.model.ORM.fortnite_cosmetics_rarity_db import FortniteCosmeticsRarityDB
from src.model.ORM.fortnite_items_db import FortniteItemsDB


def get_fortnite_cosmetic_list(
    search_param: str,
    limit: int = 0,
    base_url: str = "",
    rarity: str = "",
    type: str = "",
    price: int = -1,
) -> dict:
    """
    Search for fortnite cosmetics using a partial, case-insensitive match.

    Args:
        search_param (str): The search term to match against cosmetic names.
        limit (int): The maximum number of cosmetics to return. If 0 no limit.
        base_url (str): The base URL for generating resource URLs.
        rarity (str): Filter cosmetics by rarity (if is not empty).
        type (str): Filter cosmetics by type (if is not empty).
        price (int): Filter cosmetics by price (if is not -1).

    Returns:
        dict: A dictionary containing the list of matching cosmetics.

    """
    try:
        session = database_connection.get_database_session()

        query_fortnite_cosmetics = session.query(FortniteCosmeticDB)
        if search_param != "":
            query_fortnite_cosmetics = query_fortnite_cosmetics.filter(
                FortniteCosmeticDB.name.ilike(f"%{search_param}%")
            )
        if rarity != "":
            query_fortnite_cosmetics = query_fortnite_cosmetics.join(
                FortniteCosmeticDB.rarity_ref
            ).filter(FortniteCosmeticsRarityDB.name.ilike(f"%{rarity}%"))
        if type != "":
            query_fortnite_cosmetics = query_fortnite_cosmetics.join(
                FortniteCosmeticDB.type_ref
            ).filter(FortniteCosmeticTypesDB.type.ilike(f"%{type}%"))
        if price != -1:
            query_fortnite_cosmetics = query_fortnite_cosmetics.filter(
                FortniteCosmeticDB.price == price
            )
        query_fortnite_cosmetics = query_fortnite_cosmetics.order_by(
            FortniteCosmeticDB.id.asc()
        )

        if limit != 0:
            query_fortnite_cosmetics = query_fortnite_cosmetics.limit(limit)
        fortnite_cosmetic_list = query_fortnite_cosmetics.all()
        result = {"cosmetics": {}}
        for index, cosmetic in enumerate(fortnite_cosmetic_list):
            result["cosmetics"][index] = FortniteCosmetic(cosmetic, base_url).toJSON()

        if result == {"cosmetics": {}}:
            raise ValueError("Cosmetic not Found")
        session.close()
        return result

    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_fortnite_item_list(search_param: str, limit: int = 0, base_url: str = "") -> dict:
    """
    Search for fortnite items using a partial, case-insensitive match.

    Args:
        search_param (str): The search term to match against item names.
        limit (int): The maximum number of items to return. If 0 no limit.
        base_url (str): The base URL for generating resource URLs.

    Returns:
        dict: A dictionary containing the list of matching episodes.

    """
    try:
        session = database_connection.get_database_session()

        query_fortnite_items = session.query(FortniteItemsDB)
        if search_param != "":
            query_fortnite_items = query_fortnite_items.filter(
                FortniteItemsDB.name.ilike(f"%{search_param}%")
            )
        query_fortnite_items = query_fortnite_items.order_by(FortniteItemsDB.id.asc())
        if limit != 0:
            query_fortnite_items = query_fortnite_items.limit(limit)
        fortnite_item_list = query_fortnite_items.all()
        session.close()
        result = {"items": {}}
        for index, item in enumerate(fortnite_item_list):
            result["items"][index] = FortniteItem(item, base_url).toJSON()

        if result == {"items": {}}:
            raise ValueError("Item not Found")
        return result

    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}


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
