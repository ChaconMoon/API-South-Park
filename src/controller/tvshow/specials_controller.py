"""
Module written by Carlos Chacón.

This module get the param of the API in the get special operations,
 make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Internal Inputs
from src.controller.database_connection import get_query_result
from src.model.specials import Special


# Get one special data from the API and Return it.
def get_special_by_id(id: int, add_url=False, base_url="", metadata=False):
    """
    Get the ID of a special and returns a dict with the content of this special.

    Params:
        id (int): The id of the special in the database.
        add_url (bool): Define is the query must return the URL.
        base_url (str): The url used to create the URL API.

    Returns:
        A dict with the response or a dict with the error.

    """
    try:
        # Make the query to the Database
        query_result = get_query_result(
            text("""
                SELECT id,title,release_date,description,link,poster FROM public.specials
                where id = :id
                """),
            {"id": id},
        )

        # If the is a error in the query returns the error
        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        if query_result.rowcount == 0:
            return {"error": "Special not found", "status": "failed"}

        # Create a objet with the result of the query
        for row in query_result:
            special = Special(row, base_url)

        # Create the object with the URL
        if add_url:
            result = dict()
            result["name"] = special.model_dump()["name"]
            result["url"] = f"{base_url}api/specials/{row[0]}"
            return result

        # Create the complete object with the metadata
        query_result = get_query_result(text("SELECT * FROM public.specials"))
        return special.toJSON(metadata, query_result.rowcount)

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_random_special(base_url=""):
    """
    Return a dict with the content of a random special.

    Params:
        base_url (str): The url used to create the URL API.

    Returns:
        A dict with the response or a dict with the error.

    """
    try:
        # Make the query to the Database
        query_result = get_query_result(
            text("""
                    SELECT * FROM public.specials
                    ORDER BY RANDOM()
                    limit 1
                """)
        )
        # If the is a error in the query returns the error
        if query_result is None:
            return {"error": "Database not available", "status": "failed"}
        if query_result.rowcount == 0:
            return {"error": "Special not found", "status": "failed"}
        for row in query_result:
            special = Special(row, base_url)
        return special.toJSON()
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
