from src.model.chinpokomon import Chinpokomon
from src.controller.database_connection import get_query_result
from sqlalchemy import text


def get_chinpokomon_by_id(id: int, add_url=False, base_url="") -> dict:
    """
    Get one character of the database

    Args:
        id (int): The id of a Character.
        add_url (bool): If the response must contain the URL of the API
        base_url (str): "The URL base of the API

    Returns:
        The JSON Response

    """
    try:
        # Get one character from the database using this ID
        query_result = get_query_result(
            text("SELECT * FROM public.chinpokomon Where id=:id"), {"id": id}
        )

        # Return the errors response

        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Character not found", "status": "failed"}
        # Get the Character info
        for row in query_result:
            chinpokomon = Chinpokomon(row, base_url)
        if add_url:
            result = dict()
            result["name"] = chinpokomon.model_dump()["name"]
            result["url"] = f"{base_url}api/chinpokomon/{row[0]}"
            return result
        # Get the number of characters
        query_result = get_query_result(text("SELECT * FROM public.chinpokomon"))

        # Create API Response

        # Add Character Data to Response

        # Return Response
        return chinpokomon.toJSON()
    except Exception as e:
        return {"error": str(e), "status": "failed"}
