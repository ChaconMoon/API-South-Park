"""
Module written by Carlos Chacón.

This module get the param of the API in the get special operations, make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Internal Inputs
from src.controller.database_connection import get_query_result
from src.model.specials import Special


# Get one special data from the API and Return it.
def get_special_by_id(id: int, add_url=False, base_url=""):
    """
    Get the ID of a special and returns a dict with the content of this special in the database.

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
                SELECT id,title,release_date,description,link FROM public.specials
                where id = :id"""),
            {"id": id},
        )

        # If the is a error in the query returns the error
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        if query_result.rowcount == 0:
            return {"error": "Special not found", "status": "failed"}

        # Create a objet with the result of the query
        for row in query_result:
            special_info = Special(
                id=int(row[0]) if row[0] is not None else 0,
                title=str(row[1]) if row[1] is not None else "",
                release_date=str(row[2]) if row[2] is not None else "",
                description=str(row[3]) if row[3] is not None else "",
                link=str(row[4]) if row[4] is not None else "",
            )

        # Create the object with the URL
        if add_url:
            result = dict()
            result["name"] = special_info.model_dump()["name"]
            result["url"] = f"{base_url}special/{row[0]}"
            return result

        # Create the complete object with the metadata
        query_result = get_query_result(text("SELECT * FROM public.specials"))
        result = dict()
        result["special"] = special_info.model_dump()
        result["metadata"] = dict()
        result["metadata"]["total_specials_in_database"] = query_result.rowcount
        return result

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
