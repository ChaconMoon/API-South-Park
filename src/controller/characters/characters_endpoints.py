from fastapi import Request, Response, status, APIRouter
from src.controller.date_controller import get_today_birthday_character
from src.controller.characters.characters_controller import (
    get_character_by_id,
    get_characters_by_search,
)
from src.controller.characters.alter_ego_controller import (
    get_all_alteregos_of_a_character,
    get_alter_ego_by_character_and_id,
)
from src.controller.characters.family_controller import get_family_by_id

router = APIRouter(tags=["Characters"])


# Create the endpoint to get one alter ego of a character.
@router.get("/api/characters/{id}/alteregos/{alter_id}")
def show_alterergo(
    id: int, alter_id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the alterego of one espefic ID of one specific character.

    Returns:
    A dict with the response
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
    Get the response with the all the alteregos of one specific character.

    Returns:
    A dict with the response
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
    TESTING SEARCH IN API.
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
@router.get("/api/families/{id}", tags=["Characters"])
def show_family(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the family with a specific id.

    Returns:
    A dict with the response
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
@router.get("/api/characters/{id}", tags=["Characters"])
async def show_character(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the character with a specific id.

    Returns:
    A dict with the response
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
def get_characters_with_birthday_today(request: Request):
    return get_today_birthday_character(base_url=str(request.base_url))
