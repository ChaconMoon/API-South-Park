"""
Module written by Carlos Chacón.

This module get the param of the API in the get special operations,
 make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import func

from src.controller import database_connection

# Internal Inputs
from src.model.ORM.special_db import SpecialDB
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
        session = database_connection.get_database_session()

        special = Special(
            session.query(SpecialDB).filter(SpecialDB.id == id).first(), base_url
        )
        return special.toJSON()

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
        session = database_connection.get_database_session()

        special = Special(
            session.query(SpecialDB).order_by(func.random()).first(), base_url
        )
        return special.toJSON()
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
