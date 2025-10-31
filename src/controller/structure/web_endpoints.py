import json
from fastapi import APIRouter, Response, Request
from src.controller.characters.characters_controller import get_character_by_id
from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_footer_web import create_footer

router = APIRouter(tags=["Web"])


# Create the basic response of the API with the connection of the API.
@router.get("/")
def index(response: Response, request: Request) -> dict:
    """
    Get the response with the connection of the API.

    Returns:
    A dict with the response.
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
