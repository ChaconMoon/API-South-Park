"""
Module written by Carlos Chacón.

This module defines the Chinpokomon-related endpoints for the South Park API.
It provides routes to access information about Chinpokomon creatures that appear
in the South Park series.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.chinpokomon.chinpokomon_controller import (
    get_chinpokomon_by_id,
    get_chinpokomon_list,
    get_chinpokomon_list_by_search,
    get_random_chinpokomon,
)

router = APIRouter(tags=["Chinpokomon"])


@router.get("/api/chinpokomons")
def show_chinpokomon_list(
    request: Request, response: Response, search: str = "", limit: int = 0
):
    """
    Get a list of Chinpokomon, with optional search and limit.

    Args:
        request (Request): FastAPI request object containing base URL.
        response (Response): FastAPI response object for status codes.
        search (str): A search term to filter Chinpokomon by name.
        limit (int): The maximum number of Chinpokomon to return.

    Returns:
        dict: JSON response containing the list of Chinpokomon.

    Response Codes:
        200: Chinpokomon found and returned successfully.
        404: No Chinpokomon found for the given search criteria.
        500: Internal server error.

    """
    if search != "":
        json = get_chinpokomon_list_by_search(
            search, limit, base_url=str(request.base_url)
        )
    else:
        json = get_chinpokomon_list(limit, base_url=str(request.base_url))
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


@router.get("/api/chinpokomons/random")
def show_random_chinpokomon(request: Request, response: Response):
    """
    Get a random Chinpokomon from the database.

    Args:
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object for status codes

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
    json = get_random_chinpokomon(base_url)
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json


@router.get("/api/chinpokomons/{id}")
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
    json = get_chinpokomon_by_id(id=id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return json
