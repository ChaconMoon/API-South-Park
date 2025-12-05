"""
Module written by Carlos Chacón.

This module get the param of the API in the get family operations,
make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import func

from src.controller import database_connection
from src.model.family import Family

# Interal Inputs
from src.model.ORM.families_db import FamilyDB


def get_family_list(limit: int = 0, base_url="") -> dict:
    """
    Return a list of families.

    :param limit: The number of families returned
    :type limit: int

    :param base_url: The URL used to create the absolute URL in response.
    :type base_url: str

    :return: A dict with the families.
    :rtype: dict
    """
    try:
        session = database_connection.get_database_session()
        if limit != 0:
            family_list = session.query(FamilyDB).limit(limit).all()
        else:
            family_list = session.query(FamilyDB).all()

        result = dict()
        result["families"] = []
        result["families"].extend(
            Family(family_db, base_url=base_url) for family_db in family_list
        )

        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_family_search(search: str, limit: int = 0, base_url="") -> dict:
    """
    Retiurn the result of a family search.

    :param search: The param used in the search.
    :type search: str

    :param limit: The number of families returned.
    :type limit: int

    :param base_url: The URL used to create the absolute URL.
    :type base_url: str
    :return: A dict with the families
    :rtype: dict

    """
    try:
        session = database_connection.get_database_session()
        if limit != 0:
            family_list = (
                session.query(FamilyDB)
                .filter(FamilyDB.name.ilike((f"%{search}%")))
                .limit(limit)
                .all()
            )
        else:
            family_list = (
                session.query(FamilyDB).filter(FamilyDB.name.ilike((f"%{search}%"))).all()
            )

        result = dict()
        result["families"] = []
        result["families"].extend(
            Family(family_db, base_url=base_url) for family_db in family_list
        )

        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}


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
        session = database_connection.get_database_session()

        family = Family(
            session.query(FamilyDB).filter(FamilyDB.id == id).first(), base_url=url
        )

        # Get the result of the query to the databse.
        total_families = session.query(func.count(FamilyDB.id)).scalar()

        return family.toJSON(metadata, total_results=total_families)

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
        session = database_connection.get_database_session()
        family = Family(
            session.query(FamilyDB).order_by(func.random()).first(), base_url=base_url
        )

        return family.toJSON()

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
