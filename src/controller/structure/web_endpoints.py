"""
Module written by Carlos Chacón.

This module defines the web interface endpoints for the South Park API.
It provides routes for rendering HTML templates and serving the main index page
with API documentation and examples.
"""

import json

from fastapi import APIRouter, Request, Response

from src.controller.characters.characters_controller import get_character_by_id
from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_footer_web import create_footer

router = APIRouter(tags=["Web"])


@router.get("/")
def index(response: Response, request: Request) -> dict:
    """
    Render the main index page of the South Park API.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object containing base URL

    Returns:
        dict: Template response containing:
            - Base URL for API endpoints
            - Example API response (character with ID 100)
            - Footer HTML content

    Template Context:
        request: FastAPI request object
        base_url: Base URL for API endpoints
        example_api_response: Formatted JSON example of character endpoint
        footer: HTML content for page footer

    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "base_url": request.base_url,
            "example_api_response": json.dumps(
                get_character_by_id(100, base_url=str(request.base_url)),
                indent=4,
                ensure_ascii=False,
            ),
            "footer": create_footer(),
        },
    )
