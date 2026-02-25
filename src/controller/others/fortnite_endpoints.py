"""
Module written by Carlos Chacón.

This module defines the fortnite endpoints for the South Park API.
It provides routes to access Fortnite-related content.
"""

from fastapi import APIRouter, Query, Request, Response
from fastapi.responses import StreamingResponse
from typing_extensions import Annotated

from src.controller.others.fortnite_controller import (
    get_fortnite_cosmetic,
    get_fortnite_cosmetic_image_by_id,
    get_fortnite_item,
    get_fortnite_item_image_by_id,
    get_fortnite_item_list,
)

router = APIRouter(tags=["Others"])


@router.get("/api/fortnite/items/")
def show_fortnite_items_list(
    request: Request, response: Response, search: str = "", limit: int = 0
) -> dict:
    """
    Get a list of Fortnite items in the South Park collaboration, with optional search and limit.

    Args:
        response (Response): FastAPI response object for status codes.
        request (Request): FastAPI request object containing base URL.
        search (str): A search term to filter items by name (If is not empty).
        limit (int): The maximum number of items to return (if is not 0).

    Returns:
        dict: JSON response containing the list of items.

    Response Codes:
        200: Items found and returned successfully.
        404: No episodes found for the given search criteria.
        500: Internal server error.

    """
    return get_fortnite_item_list(
        search_param=search, base_url=str(request.base_url), limit=limit
    )


@router.get("/api/fortnite/items/{item_id}/image")
def return_fornite_item(
    item_id: str,
    size: Annotated[str, Query(regex="^(original|small|medium|large)$")] = "original",
) -> StreamingResponse:
    """
    Docstring for return_fornite_item.

    :param item_id: Description
    :type item_id: str
    :param size: Description
    :type size: Annotated[str, Query(regex="^(original|small|medium|large)$")]
    :return: Description
    :rtype: StreamingResponse
    """
    return get_fortnite_item_image_by_id(item_id=item_id, image_size=size)


@router.get("/api/fortnite/items/{item_id}")
def return_fortnite_item(
    item_id: str, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Return Fortnite item details based on the provided item ID.

    Args:
        item_id (str): Unique identifier for the Fortnite item
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object
        metadata (bool): If the response must contain metadata.

    Returns:
        dict: JSON response containing either:
            - Fortnite item details if found
            - Error message if item ID is not recognized
    Response Format:
        Success:
            {
                "id": str,
                "name": str,
                "type": str,
                "rarity": str,
                "description": str,
                "images": dict,
                "effect": str,
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    base_url = str(request.base_url)
    fortnite_item = get_fortnite_item(
        item_id=item_id, base_url=base_url, metadata=metadata
    )
    if "error" in fortnite_item:
        if fortnite_item["status"] == "Not Found":
            response.status_code = 404
        if fortnite_item["status"] == "failed":
            response.status_code = 500
    return fortnite_item


@router.get("/api/fortnite/cosmetics/{cosmetic_id}/image")
def get_fortnite_cosmetic_image(
    cosmetic_id: int,
    request: Request,
    response: Response,
    size: Annotated[str, Query(regex="^(original|small|medium|large)$")] = "original",
) -> StreamingResponse:
    """
    Docstring for get_fortnite_cosmetic_image.

    :param cosmetic_id: Description
    :type cosmetic_id: str
    :param request: Description
    :type request: Request
    :param response: Description
    :type response: Response
    :param size: Description
    :type size: Annotated[str, Query(regex="^(original|small|medium|large)$")]
    :return: Description
    :rtype: StreamingResponse
    """
    return get_fortnite_cosmetic_image_by_id(cosmetic_id=cosmetic_id, image_size=size)


@router.get("/api/fortnite/cosmetics/{cosmetic_id}")
def return_fortnite_cosmetic(
    cosmetic_id: str, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Return Fortnite cosmetic details based on the provided cosmetic ID.

    Args:
        cosmetic_id (str): Unique identifier for the Fortnite cosmetic
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object
        metadata (bool): If the response must contain metadata.

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
                "description": str,
                "images": dict,
                }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    base_url = str(request.base_url)

    fortnite_cosmetic = get_fortnite_cosmetic(
        cosmetic_id=cosmetic_id, base_url=base_url, metadata=metadata
    )
    if "error" in fortnite_cosmetic:
        if fortnite_cosmetic["status"] == "Not Found":
            response.status_code = 404
        if fortnite_cosmetic["status"] == "failed":
            response.status_code = 500

    return fortnite_cosmetic
