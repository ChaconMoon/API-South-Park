"""
Module written by Carlos Chacón.

This module get the param of the API in the get family operations,
make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Interal Inputs
from src.controller.database_connection import get_query_result
from src.model.family import Family


# Connection with the database
def get_family_by_id(id: int, url="", metadata=False) -> dict:
    """
    Get the ID of one familiy at return the data of this family and all they members.

    Params:
        id (int): The id of the family.
        url (str): The URL used.
    Retruns:
        A dict with the data of the family.
    """
    # Create variable to store the result data.
    try:
        # Get the result of the query to the databse.
        query_result = get_query_result(
            text("""SELECT characters.id,characters.name,families.name, families.images
                    FROM public.characters,public.families
                    Where characters.family = families.id And families.id = :id
                    order by characters.id asc"""),
            {"id": id},
        )

        # Get all the rows of the query result.
        rows = query_result.fetchall()

        # Add all the family members to the array.
        for _row in rows:
            family = Family(rows, url, id)

        return family.toJSON(metadata, total_results=query_result.rowcount)

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
