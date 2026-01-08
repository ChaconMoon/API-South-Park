"""
Module writted by Carlos Chacón.

This module defines miscellaneous endpoints for the South Park API.
These endpoints provide various additional functionalities that do not
fit into other specific categories.
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.controller.others.miscellaneous_controller import get_butters_punishment_by_id

router = APIRouter(tags=["Others"])

@router.get("/api/butterspunishments/{id}")
def show_butters_punishment(id: int, request: Request) -> JSONResponse:
    """
    Retrieve a Butters' punishment entry by its unique ID.

    Args:
        id (int): Unique identifier for the punishment
        request (Request): FastAPI request object containing base URL
        response (Response): FastAPI response object

    Returns:
        dict: JSON response containing the Butters'
          punishment data or an error message if not found

    """
    base_url = str(request.base_url)
    response = get_butters_punishment_by_id(id=id, base_url=base_url)

    if "error" in response:
        if response["error"] == f"Butters' punishment with ID {id} not found.":
            return JSONResponse(
                status_code=404,
                content=response
            )
        if response["error"] == "An error occurred while retrieving the punishment.":
            return JSONResponse(
                status_code=500,
                content=response
            )
    else:
        return JSONResponse(
            status_code=200,
            content=response
        )
