"""
Module written by Carlos Chacón.

This module handles database operations for retrieving Chinpokomon information.
It provides functions to fetch specific Chinpokomon by ID from the database.
"""

from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from src.controller import database_connection
from src.model.chinpokomon import Chinpokomon
from src.model.ORM.chinpokomon_db import ChinpokomonDB


def get_chinpokomon_list(limit: int = 0, base_url: str = "") -> dict:
    """
    Get a list of all Chinpokomon, ordered by ID.

    Args:
        limit (int): The maximum number of Chinpokomon to return. If 0, no limit.
        base_url (str): The base URL for generating resource URLs.

    Returns:
        dict: A dictionary containing the list of Chinpokomon.

    """
    session = database_connection.get_database_session()
    try:
        chinpokomon_query = session.query(ChinpokomonDB).order_by(ChinpokomonDB.id)
        if limit != 0:
            chinpokomon_query = chinpokomon_query.limit(limit)
        chinpokomon_list_db = chinpokomon_query.all()
        if chinpokomon_list_db == []:
            raise AttributeError("Chinpokomon Not Found")
        result = {"chinpokomons": {}}
        for index, chinpokomon_db in enumerate(chinpokomon_list_db):
            chinpokomon = Chinpokomon(chinpokomon_db, base_url)
            result["chinpokomons"][index] = chinpokomon.toJSON()
        return result
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_chinpokomon_list_by_search(
    search: str, limit: int = 0, base_url: str = ""
) -> dict:
    """
    Search for Chinpokomon by name using a partial, case-insensitive match.

    Args:
        search (str): The search term to match against Chinpokomon names.
        limit (int): The maximum number of Chinpokomon to return. If 0, no limit.
        base_url (str): The base URL for generating resource URLs.

    Returns:
        dict: A dictionary containing the list of matching Chinpokomon.

    """
    session = database_connection.get_database_session()
    try:
        chinpokomon_query = (
            session.query(ChinpokomonDB)
            .filter(ChinpokomonDB.name.ilike(f"%{search}%"))
            .order_by(ChinpokomonDB.id)
        )
        if limit != 0:
            chinpokomon_query = chinpokomon_query.limit(limit)
        chinpokomon_list_db = chinpokomon_query.all()
        if chinpokomon_list_db == []:
            raise AttributeError("Chinpokomon Not Found")
        result = {"chinpokomons": {}}
        for index, chinpokomon_db in enumerate(chinpokomon_list_db):
            chinpokomon = Chinpokomon(chinpokomon_db, base_url)
            result["chinpokomons"][index] = chinpokomon.toJSON()
        return result
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_chinpokomon_by_id(
    id: int, add_url: bool = False, base_url: str = "", metadata: bool = False
) -> dict:
    """
    Retrieve a specific Chinpokomon from the database by its ID.

    Args:
        id (int): The unique identifier of the Chinpokomon
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints
        metadata (bool): Whether to include metadata in response

    Returns:
        dict: JSON response containing either:
            - Chinpokomon data if found
            - Error message if not found or database error

    Response Format:
        Success with add_url=True:
            {
                "name": str,
                "url": str
            }

        Success with add_url=False:
            {
                "id": int,
                "name": str,
                "image": str
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        chinpokomon_db = (
            session.query(ChinpokomonDB).filter(ChinpokomonDB.id == id).first()
        )
        if chinpokomon_db is None:
            raise AttributeError("Chinpokomon Not Found")
        chinpokomon = Chinpokomon(chinpokomon_db, base_url)

        if add_url:
            return {
                "name": chinpokomon.model_dump()["name"],
                "url": f"{base_url}api/chinpokomons/{id}",
            }
        chinpokomon_count = session.query(ChinpokomonDB).count()
        return chinpokomon.toJSON(metadata, chinpokomon_count)
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_chinpokomon(base_url=""):
    """
    Get a Random Chinpokomon from the Database.

    Args:
        base_url (str): The base URL for API endpoints

    Returns:
        dict: JSON response containing either:
            - Chinpokomon data if found
            - Error message if not found or database error

    Response Format:

    Success:
            {
                "id": int,
                "name": str,
                "image": str
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    session = database_connection.get_database_session()
    try:
        chinpokomon_db = session.query(ChinpokomonDB).order_by(func.random()).first()
        if chinpokomon_db is None:
            raise AttributeError("Chinpokomon Not Found")
        chinpokomon = Chinpokomon(chinpokomon_db, base_url)
        return chinpokomon.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
