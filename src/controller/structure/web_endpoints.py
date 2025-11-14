"""
Module written by Carlos Chacón.

This module defines the web interface endpoints for the South Park API.
It provides routes for rendering HTML templates and serving the main index page
with API documentation and examples.
"""

import json

import toon
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from markdown import markdown

from src.controller.characters.characters_controller import get_character_by_id
from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_changelog_buttons import create_changelog_links
from src.website_elements.create_footer_web import create_footer
from src.website_elements.create_post_card_grid import (
    get_intro_in_menu,
    get_title_in_menu,
)

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


@router.get("/changelog/{entry}")
def create_changelog(request: Request, response: Response, entry: str):
    """
    Render a Post in the Changelog.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object containing base URL
        entry (str): Entry file name

    Returns:
        A HTML Template with the response

    Template Context:
        request: FastAPI request object
        base_url: Base URL for API endpoints
        changelog_item: The Item with the Changelog entry
        footer: HTML content for page footer

    """
    try:
        with open(f"./docs/changelog_posts/{entry}.MD", encoding="utf-8") as f:
            markdown_content = f.read()
        changelog_item = markdown(
            markdown_content,
            extensions=["fenced_code", "tables", "attr_list", "md_in_html"],
        )
        changelog_item = changelog_item.replace("<p><img", "<img")
        changelog_item = changelog_item.replace('webp" /></p>', 'webp" />')
    except FileNotFoundError:
        raise HTTPException(status_code=404) from None  # Investigate exception chaining
    return templates.TemplateResponse(
        "changelog_page.html",
        context={
            "request": request,
            "changelog_item": changelog_item,
            "base_url": request.base_url,
            "articule_title_in_social_media": get_title_in_menu("Version_0.2.MD"),
            "articule_description_in_social_media": get_intro_in_menu("Version_0.2.MD"),
            "url_in_social_media": f"{str(request.base_url).replace('http://', 'https://')}changelog/",
            "changelog_links": create_changelog_links(f"{entry}.MD"),
            "footer": create_footer(),
        },
    )


@router.get("/changelog")
def go_to_last_changelog():
    """
    Redirect to the latest changelog entry listed in data/changelog_order.toon.

    If the file or the posts list is missing or empty, return 404.
    """
    try:
        with open("data/changelog_order.toon") as f:
            toon_file = toon.decode(f.read())
            posts = toon_file["posts"]
            if not posts:
                raise HTTPException(status_code=404)
            # Use the last entry in the list as the "latest"
            last = str(posts[0])
            # Remove trailing .MD if present (Python 3.9+)
            if last.endswith(".MD"):
                last = last.removesuffix(".MD")
            return RedirectResponse(url=f"/changelog/{last}", status_code=307)
    except FileNotFoundError:
        raise HTTPException(status_code=404) from None
    except KeyError:
        raise HTTPException(status_code=404) from None
