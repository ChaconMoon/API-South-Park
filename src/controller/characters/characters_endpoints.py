"""
Module written by Carlos Chacón.

This module defines the character-related endpoints for the South Park API.
It provides routes to access information about characters, their alter egos,
families, and birthday events.
"""

from fastapi import APIRouter, Request, Response, status

from src.controller.characters.alter_ego_controller import (
    get_all_alteregos_of_a_character,
    get_alter_ego_by_character_and_id,
)
from src.controller.characters.characters_controller import (
    get_all_characters_with_alterego,
    get_character_by_id,
    get_characters_by_search,
    get_random_character,
)
from src.controller.characters.family_controller import get_family_by_id
from src.controller.date_controller import get_today_birthday_character

router = APIRouter(tags=["Characters"])


# Create the Endpoint that returns a random character
@router.get("/api/characters/random")
def show_random_character(
    request: Request,
    response: Response,
    exclude_famous_guests: bool = False,
):
    """
    Get a random character's information.

    Args:
        request (Request): FastAPI request object
        response (Response): FastAPI response object
        exclude_famous_guests: If true excludes the famous guests from the random search

    Returns:
        dict: JSON response with character data or error

    Response Codes:
        200: Character found
        404: Character not found
        500: Database error

    """
    json = get_random_character(
        exclude_famous_guests=exclude_famous_guests, base_url=str(request.base_url)
    )
    if "error" in json:
        if json["error"] == "Character not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK

    return json


# Create the endpoint to get one alter ego of a character.
@router.get("/api/characters/{id}/alteregos/{alter_id}")
def show_alterergo(
    id: int, alter_id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific alter ego of a character.

    Args:
        id (int): Character ID
        alter_id (int): Alter ego ID
        request (Request): FastAPI request object
        response (Response): FastAPI response object
        metadata (bool): Whether to include metadata

    Returns:
        dict: JSON response with alter ego data or error


    Response Codes:
        200: Alter ego found
        404: Alter ego not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_alter_ego_by_character_and_id(
        id_character=id, id_alter_ego=alter_id, base_url=base_url, metadata=metadata
    )
    if "error" in json:
        if json["error"] == "Alter Ego not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alterego" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the endpoint to get all the alteregos of a character.
@router.get("/api/characters/{id}/alteregos")
def show_all_alteregos(id: int, request: Request, response: Response) -> dict:
    """
    Get all alter egos of a character.

    Args:
        id (int): Character ID
        request (Request): FastAPI request object
        response (Response): FastAPI response object

    Returns:
        dict: JSON response with all alter egos or error

    Response Codes:
        200: Alter egos found
        404: No alter egos found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_all_alteregos_of_a_character(id_character=id, base_url=base_url)
    if json is None:
        json = {"error": "Alter Egos not found", "status": "failed"}
    if "error" in json:
        if json["error"] == "Alter Egos not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alteregos" in json:
            response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/search/characters/{search_param}")
def search_character(
    response: Response,
    request: Request,
    search_param: str,
    metadata: bool = False,
    limit: int = 10,
) -> dict:
    """
    Search for characters by name.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object
        search_param (str): Search query string
        metadata (bool): Whether to include metadata
        limit (int): Maximum number of results to return

    Returns:
        dict: JSON response with matching characters or error

    Response Codes:
        200: Characters found
        404: No matches found
        500: Database error

    """
    json = get_characters_by_search(
        search_param=search_param,
        base_url=str(request.base_url),
        limit=limit,
    )
    if "error" in json:
        if json["error"] == "Character not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


# Create the endpoint to get the families.
@router.get("/api/families/{id}")
def show_family(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific family's information.

    Args:
        id (int): Family ID
        request (Request): FastAPI request object
        response (Response): FastAPI response object
        metadata (bool): Whether to include metadata

    Returns:
        dict: JSON response with family data or error

    Response Codes:
        200: Family found
        404: Family not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_family_by_id(id, url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Family not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "family" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the endpoint to get the characters.
@router.get("/api/characters/{id}")
async def show_character(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get a specific character's information.

    Args:
        id (int): Character ID
        request (Request): FastAPI request object
        response (Response): FastAPI response object
        metadata (bool): Whether to include metadata

    Returns:
        dict: JSON response with character data or error

    Response Codes:
        200: Character found
        404: Character not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_character_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Character not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/todaybirthdays")
def get_characters_with_birthday_today(request: Request, response: Response) -> dict:
    """
    Get all characters whose birthday is today.

    Args:
        request (Request): FastAPI request object
        response (Response): FastAPI response object

    Returns:
        dict: JSON response with characters having birthdays today

    Response Codes:
        200: Character found
        404: No one has their birthday today
        500: Database error

    """
    json = get_today_birthday_character(base_url=str(request.base_url))
    if "error" in json:
        if json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "message" in json:
        if json["message"] == "No one has their birthday today":
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/characterswithalterego")
def get_characters_on_alterego_table(request: Request, response: Response) -> dict:
    """
    Get all characters that have a alter ego.

    Args:
        request (Request): FastAPI request object
        response (Response): FastAPI response object

    Returns:
        dict: JSON response with characters with alterego

    Response Codes:
        200: Character found
        404: Empty alterego database found
        500: Database not avalible error

    """
    json = get_all_characters_with_alterego(base_url=str(request.base_url))
    if "error" in json:
        if json["error"] == "Query error. No Alteregos in database":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json
