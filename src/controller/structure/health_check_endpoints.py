"""
Module written by Carlos Chacón.

This module defines the health check endpoints for the South Park API.
It provides routes to check the API's status and database connectivity.
"""

from fastapi import APIRouter, Response, status

from src.controller.database_status import get_database_status

router = APIRouter(tags=["Health Check"])


@router.get("/api/")
def api_index(response: Response) -> dict:
    """
    Get the API health status and database connection state.

    Args:
        response (Response): FastAPI response object for setting status codes

    Returns:
        dict: JSON response containing either:
            - API status and database connection info if healthy
            - Error message if database connection failed

    Response Codes:
        200: API is healthy and database is connected
        500: Database connection error

    Response Format:
        Success:
            {
                "status": "ok",
                "database": "connected"
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    json = get_database_status()

    if "error" in json:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json
