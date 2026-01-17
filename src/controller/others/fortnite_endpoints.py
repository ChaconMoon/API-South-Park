"""
Module written by Carlos Chacón.

This module defines the fortnite endpoints for the South Park API.
It provides routes to access Fortnite-related content.
"""
from fastapi import APIRouter, Request, Response

from src.controller.others.fortnite_controller import (
    get_fortnite_cosmetic,
    get_fortnite_item,
)

router = APIRouter(tags=["Others"])
@router.get("/api/fortnite/item/{item_id}")
def return_fortnite_item(item_id: str, request: Request, response: Response) -> dict:
    """
    Return Fortnite item details based on the provided item ID.

    Args:
        item_id (str): Unique identifier for the Fortnite item
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object

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
    return get_fortnite_item(item_id=item_id, base_url=base_url)

@router.get("/api/fortnite/cosmetic/{cosmetic_id}")
def return_fortnite_cosmetic(cosmetic_id: str, request: Request, response: Response) -> dict:
    """
    Return Fortnite cosmetic details based on the provided cosmetic ID.

    Args:
        cosmetic_id (str): Unique identifier for the Fortnite cosmetic
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object

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

    return get_fortnite_cosmetic(cosmetic_id=cosmetic_id, base_url=base_url)
