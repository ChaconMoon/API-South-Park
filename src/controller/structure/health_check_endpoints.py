from fastapi import APIRouter, Response, Request, status

from src.controller.database_status import get_database_status

router = APIRouter(tags=["Health Check"])


# Create the basic response of the API with the connection of the API.
@router.get("/api/")
def api_index(response: Response) -> dict:
    """
    Get the response with the connection of the API.

    Returns:
    A dict with the response.
    """
    json = get_database_status()

    if "error" in json:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json
