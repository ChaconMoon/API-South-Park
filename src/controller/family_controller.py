"""
Module written by Carlos Chacón.

This module get the param of the API in the get family operations, make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Interal Inputs
from src.controller.data_controller import parse_array_to_list
from src.controller.character_controller import get_character_by_id
from src.controller.database_connection import get_query_result
from src.model.family import Family


# Connection with the database
def get_family_by_id(id: int, url="") -> dict:
    """
    Get the ID of one familiy at return the data of this family and all they members.

    Params:
        id (int): The id of the family.
        url (str): The URL used.
    Retruns:
        A dict with the data of the family.
    """
    # Create variable to store the result data.
    result = dict()
    family_members = []
    try:
        # Get the result of the query to the databse.
        query_result = get_query_result(
            text("""SELECT characters.id,characters.name,families.name, families.images FROM public.characters,public.families
                                        Where characters.family = families.id And families.id = :id order by characters.id asc"""),
            {"id": id},
        )

        # Get all the rows of the query result.
        rows = query_result.fetchall()

        # Add all the family members to the array.
        for row in rows:
            family_members.append(
                get_character_by_id(int(row[0]), add_url=True, base_url=url)
            )
        # Create de dict with the response.
        query_result = get_query_result(text("SELECT * FROM public.families"))
        family = Family(
            id=id,
            name=str(rows[0][2]),
            images=[
                f"{url}{image_url}" for image_url in parse_array_to_list(rows[0][3])
            ],
        )
        result["family"] = family.model_dump()
        result["family"]["members"] = family_members
        result["metadata"] = dict()
        result["metadata"]["total_families_in_database"] = query_result.rowcount

        return result

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
