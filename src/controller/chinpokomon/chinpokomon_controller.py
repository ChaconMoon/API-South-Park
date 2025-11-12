"""
Module written by Carlos Chacón.

This module handles database operations for retrieving Chinpokomon information.
It provides functions to fetch specific Chinpokomon by ID from the database.
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.chinpokomon import Chinpokomon


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
    try:
        query_result = get_query_result(
            text("SELECT * FROM public.chinpokomon Where id=:id"), {"id": id}
        )

        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Chinpokomon not found", "status": "failed"}

        for row in query_result:
            chinpokomon = Chinpokomon(row, base_url)

        if add_url:
            return {
                "name": chinpokomon.model_dump()["name"],
                "url": f"{base_url}api/chinpokomon/{row[0]}",
            }
        query_result = get_query_result(text("SELECT * FROM public.chinpokomon"))

        return chinpokomon.toJSON(metadata, total_results=query_result.rowcount)

    except Exception as e:
        return {"error": str(e), "status": "failed"}
