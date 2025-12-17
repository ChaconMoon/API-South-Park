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
    get_random_alterego,
)
from src.controller.characters.characters_controller import (
    get_all_characters_with_alterego,
    get_character_by_id,
    get_characters_by_search,
    get_characters_list,
    get_random_character,
)
from src.controller.characters.family_controller import (
    get_family_by_id,
    get_family_list,
    get_family_search,
    get_random_family,
)
from src.controller.characters.groups_controller import (
    get_group_by_id,
    get_group_list,
    get_group_list_by_search,
    get_random_group,
)
from src.controller.date_controller import get_today_birthday_character

router = APIRouter(tags=["Characters"])


@router.get("/api/groups")
def show_group_list(
    request: Request, response: Response, search: str = "", limit: int = 0
):
    """
    Get a list of character groups, with optional search and limit.

    Args:
        request (Request): FastAPI request object containing base URL.
        response (Response): FastAPI response object for status codes.
        search (str): A search term to filter groups by name.
        limit (int): The maximum number of groups to return.

    Returns:
        dict: JSON response containing the list of groups.

    Response Codes:
        200: Groups found and returned successfully.
        404: No groups found for the given search criteria.
        500: Internal server error.

    """
    if search != "":
        json = get_group_list_by_search(
            base_url=str(request.base_url), limit=limit, search=search
        )
    else:
        json = get_group_list(base_url=str(request.base_url), limit=limit)

    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/groups/random")
def show_random_group(request: Request, response: Response, metadata=False):
    """
    Get a group from the database.

    Args:
        request (Request): FastAPI request object.
        response (Response): FastAPI response object.
        id (int): id of the group.
        metadata (bool): if the response must return metadata.

    Returns:
        dict: Json response with the group data.

    """
    json = get_random_group(str(request.base_url))

    if "error" in json:
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK

    return json


@router.get("/api/groups/{id}")
def show_group(request: Request, response: Response, id, metadata=False):
    """
    Get a group from the database.

    Args:
        request (Request): FastAPI request object.
        response (Response): FastAPI response object.
        id (int): id of the group.
        metadata (bool): if the response must return metadata.

    Returns:
        dict: Json response with the group data.

    """
    json = get_group_by_id(id, str(request.base_url), metadata)

    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK

    return json


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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
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
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alterego" in json:
            response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/characters")
def show_character_list(
    response: Response,
    request: Request,
    search: str = "",
    limit: int = 0,
) -> dict:
    """
    Search for characters by name.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object
        search (str): Search query string
        metadata (bool): Whether to include metadata
        limit (int): Maximum number of results to return

    Returns:
        dict: JSON response with matching characters or error

    Response Codes:
        200: Characters found
        404: No matches found
        500: Database error

    """
    if search != "":
        if limit == 0:
            limit = 10
        json = get_characters_by_search(
            search_param=search, base_url=str(request.base_url), limit=limit
        )
    else:
        json = get_characters_list(base_url=str(request.base_url), limit=limit)
    if "error" in json:
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        if json["status"] == "No characters found":
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/families")
def show_family_list(response: Response, request: Request, search="", limit=0):
    """
    Return a Family list.

    :param response: the object that contains the response to the API.
    :type response: Response
    :param request: The Object that contains the request to the API.
    :type request: Request
    :param search: The param used to search family.
    :type search: str
    :param limit: The numbers of families returned.
    :type limit: int
    """
    if search == "":
        result = get_family_list(base_url=str(request.base_url), limit=limit)
    else:
        result = get_family_search(search, limit, base_url=str(request.base_url))

    if "error" in result:
        if result["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if result["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result


@router.get("/api/families/random")
def show_random_family(response: Response, request: Request):
    """
    Get a random family's information.

    Args:
        request (Request): FastAPI request object
        response (Response): FastAPI response object
    Returns:
        dict: JSON response with family data or error

    Response Codes:
        200: Family found
        404: Family not found
        500: Database error

    """
    json = get_random_family(base_url=str(request.base_url))
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            response.status_code = status.HTTP_200_OK
    return json


@router.get("/api/alteregos/random")
def show_random_alterego(request: Request, response: Response, character: int = 0):
    """
    Get a specific alter ego of a character.

    Args:
        character (int): If is not 0, return limits the search to one character
        request (Request): FastAPI request object
        response (Response): FastAPI response object
        dict: JSON response with alter ego data or error


    Response Codes:
        200: Alter ego found
        404: Alter ego not found
        500: Database error

    """
    base_url = str(request.base_url)
    json = get_random_alterego(character, base_url)
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
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
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
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
        if json["status"] == "Database Not Available":
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
        500: Database not available error

    """
    json = get_all_characters_with_alterego(base_url=str(request.base_url))
    if "error" in json:
        if json["status"] == "Not Found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["status"] == "Database Not Available":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json
