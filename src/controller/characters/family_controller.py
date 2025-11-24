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

        # Get the result of the query to the databse.
        query_result = get_query_result(text("""SELECT * FROM public.families"""))

        return family.toJSON(metadata, total_results=query_result.rowcount)

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_random_family(base_url="") -> dict:
    """
    Get one random familiy at return the data of this family and all they members.

    Params:
        base_url (str): The URL used.
    Retruns:
        A dict with the data of the family.
    """
    # Create variable to store the result data.
    try:
        # Get the result of the query to the databse.
        query_result = get_query_result(
            text("""
                    WITH random_family AS (
                        SELECT id
                        FROM public.families
                        ORDER BY RANDOM()
                        LIMIT 1
                    )
                    SELECT c.id,
                        c.name,
                        f.name AS family_name,
                        f.images,
                        f.id
                    FROM public.characters c
                    JOIN public.families f ON c.family = f.id
                    WHERE (c.family = (SELECT id FROM random_family))
                    OR NOT EXISTS (
                            SELECT 1
                            FROM public.characters
                            WHERE family = (SELECT id FROM random_family)
                        )
                    ORDER BY c.id ASC;
                """)
        )

        # Get all the rows of the query result.
        rows = query_result.fetchall()

        # Add all the family members to the array.
        for _row in rows:
            id = rows[0][4]
            family = Family(rows, base_url, id)

        return family.toJSON()

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
