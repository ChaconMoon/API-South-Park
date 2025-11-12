"""
Module written by Carlos Chacón.

This module defines the Chinpokomon-related endpoints for the South Park API.
It provides routes to access information about Chinpokomon creatures that appear
in the South Park series.
"""

from fastapi import APIRouter, Request, Response

from src.controller.chipokomon.chinpokomon_controller import get_chinpokomon_by_id

router = APIRouter(tags=["Chinpokomon"])


@router.get("/api/chinpokomon/{id}")
def show_chinpokomon(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific Chinpokomon by ID.

    Args:
        id (int): The ID of the Chinpokomon to retrieve
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes
        metadata (bool): Whether to include metadata

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
    base_url = str(request.base_url)
    return get_chinpokomon_by_id(id=id, base_url=base_url, metadata=metadata)
