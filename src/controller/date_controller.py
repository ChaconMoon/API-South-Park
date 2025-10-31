from datetime import datetime
from sqlalchemy import text
from src.controller.characters.alter_ego_controller import (
    get_all_alteregos_of_a_character,
)
from src.controller.tvshow.episodes_controller import get_episode_by_id
from src.model.characters import Character
from src.controller.data_controller import parse_array_to_list
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
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"message": "No one has they bithday today", "status": "failed"}
        # Get the Character info
        result = dict()
        result["characters"] = list(dict())
        for row in query_result:
            id = int(row[0]) if row[0] is not None else 0
            character = Character(
                id=id,
                name=str(row[1]) if row[1] is not None else "",
                friend_group=int(row[2]) if row[2] is not None else None,
                family=int(row[3]) if row[3] is not None else None,
                birthday=str(row[4]) if row[4] is not None else None,
                age=int(row[5]) if row[5] is not None else None,
                religion=parse_array_to_list(row[6]),
                first_apperance=get_episode_by_id(
                    int(row[7]), add_url=True, base_url=base_url
                ),
                images=parse_array_to_list(row[8], is_url=True, base_url=base_url),
                alter_egos=get_all_alteregos_of_a_character(
                    id, add_url=True, base_url=base_url
                ),
                famous_guest=bool(row[9]) if row[9] is not None else False,
            )
            # Create API Response

            # Add Character Data to Response
        result["characters"].append(character.model_dump())
        # Return Response
        return result
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
