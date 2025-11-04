"""
Module written by Carlos Chacón.

This module defines the custom 404 error handler for the South Park API.
It provides different responses for API endpoints versus web interface routes
when a requested resource is not found.
"""

from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse

from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_404_image_web import get_404_image
from src.website_elements.create_footer_web import create_footer


async def custom_404_handler(request: Request, exc) -> JSONResponse | HTMLResponse:
    """
    Handle 404 Not Found errors with custom responses.

    Provides two different types of responses:
    1. JSON response for API endpoints (/api/*)
    2. HTML template response for web interface routes

    Args:
        request (Request): FastAPI request object containing URL info
        exc: Exception that triggered the 404 error

    Returns:
        JSONResponse: For API routes, returns a JSON error message
        TemplateResponse: For web routes, returns a custom 404 page with:
            - Random 404 image
            - Page footer

    Response Format:
        API Routes (/api/*):
            {"error": "Not Found"}
        Web Routes:
            HTML template with custom 404 page

    """
    path = request.url.path

    if path.startswith("/api/"):
        return JSONResponse(status_code=404, content={"error": "Not Found"})

    else:
        return templates.TemplateResponse(
            "404.html",
            context={
                "request": request,
                "image_404": f'<img id="Not_Found_Image" src="{get_404_image()}">',
                "footer": create_footer(),
            },
            status_code=404,
        )
