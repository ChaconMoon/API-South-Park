"""
Module written by Carlos Chacón.

This module defines the easter egg endpoints for the South Park API.
It provides routes to access hidden features and special content based on
specific keyword inputs.
"""

from fastapi import APIRouter, Request, Response

from src.controller.others.easter_egg_controller import get_easter_egg

router = APIRouter(tags=["Others"])


@router.get("/api/easteregg/{name}", tags=["Others"])
def return_easter_egg(name: str, request: Request, response: Response) -> dict:
    """
    Return a special easter egg response based on the provided name.

    Args:
        name (str): Keyword to trigger specific easter egg content
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object

    Returns:
        dict: JSON response containing either:
            - Easter egg content if keyword is valid
            - Error message if keyword is not recognized

    Response Format:
        Success:
            {
                "message": str,
                "image": str (optional)
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    base_url = str(request.base_url)
    return get_easter_egg(name=name, base_url=base_url)
