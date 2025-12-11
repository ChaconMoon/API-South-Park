"""
Module written by Carlos Chacón.

This module get the param of the API in the get special operations,
 make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import OperationalError

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
    session = database_connection.get_database_session()
    try:
        special_db = session.query(SpecialDB).filter(SpecialDB.id == id).first()
        special = Special(special_db, base_url)

        special_count = session.query(SpecialDB).count()
        return special.toJSON(metadata, special_count)

    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_special(base_url=""):
    """
    Return a dict with the content of a random special.

    Params:
        base_url (str): The url used to create the URL API.

    Returns:
        A dict with the response or a dict with the error.

    """
    session = database_connection.get_database_session()
    try:
        special_db = session.query(SpecialDB).order_by(func.random()).first()
        special = Special(special_db, base_url)
        return special.toJSON()
    # Control exceptions
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
