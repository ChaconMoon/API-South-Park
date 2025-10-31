from fastapi import APIRouter, Request, Response, status

from src.controller.games.game_controller import get_game_by_id

router = APIRouter(tags=["Games"])


# Create the endpoint to get all the alteregos of a character.
@router.get("/api/games/{id}/")
def show_game(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the all the alteregos of one specific character.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_game_by_id(id=id, base_url=base_url, metadata=metadata)
    if json is None:
        json = {"error": "Game not found", "status": "failed"}
    if "error" in json:
        if json["error"] == "Game not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alteregos" in json:
            response.status_code = status.HTTP_200_OK
    return json
