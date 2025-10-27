from datetime import datetime
from sqlalchemy import text
from src.controller.character_controller import create_character
from src.controller.database_connection import get_query_result


def get_today_birthday():
    actual_date = datetime.now()
    month = actual_date.strftime("%B")
    day = actual_date.strftime("%d")

    match day:
        case day if day in ["1", "21", "31"]:
            day += "st"
        case day if day in ["2", "22"]:
            day += "nd"
        case day if day in ["3", "23"]:
            day += "rd"
        case _:
            day += "th"

    return f"{month} {day}"


def get_today_birthday_character(base_url="") -> dict:
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
            text("SELECT * FROM public.characters where birthday =:birthday"),
            {"birthday": get_today_birthday()},
        )

        # Return the errors response

        if query_result is None:
            return {"error": "Database not avalible, try press F5", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"message": "No one has they bithday today", "status": "failed"}
        # Get the Character info
        result = dict()
        result["characters"] = list(dict())
        for row in query_result:
            # Create API Response
            character = create_character(row, base_url)

            # Add Character Data to Response
            result["characters"].append(character.model_dump())
        # Return Response
        return result
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
