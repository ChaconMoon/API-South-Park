"""
Module written by Carlos Chacón.

This module define the methods used to create the response of a Group item
"""

from sqlalchemy import func
from sqlalchemy.exc import (
    DataError,
    InvalidRequestError,
    OperationalError,
    ProgrammingError,
)

from src.controller import database_connection
from src.model.group import Group
from src.model.ORM.groups_db import GroupDB


def get_group_list_by_search(base_url: str, limit: int = 0, search: str = ""):
    """
    Search for groups by name using a partial, case-insensitive match.

    Args:
        base_url (str): The base URL for generating resource URLs.
        limit (int): The maximum number of groups to return. If 0, no limit.
        search (str): The search term to match against group names.

    Returns:
        dict: A dictionary containing the list of matching groups.

    """
    session = database_connection.get_database_session()
    try:
        group_query = (
            session.query(GroupDB)
            .filter(GroupDB.name.ilike(f"%{search}%"))
            .order_by(GroupDB.id)
        )
        if limit != 0:
            group_query = group_query.limit(limit)
        group_list = group_query.all()

        result = {"groups": {}}

        for index, group_db in enumerate(group_list):
            group = Group(group_db, base_url)
            result["groups"][index] = group
        if result == {"groups": {}}:
            raise ValueError("Not groups found with this value")
        return result
    except (OperationalError, ProgrammingError, InvalidRequestError, DataError) as e:
        return {"error": str(e), "status": "Database query error"}
    except (TypeError, AttributeError) as e:
        return {"error": str(e), "status": "Error processing group data"}
    except ValueError as e:
        return {"error": str(e), "status": "Not found"}
    finally:
        session.close()


def get_group_list(base_url: str, limit: int = 0):
    """
    Get a list of all groups, ordered by ID.

    Args:
        base_url (str): The base URL for generating resource URLs.
        limit (int): The maximum number of groups to return. If 0, no limit.

    Returns:
        dict: A dictionary containing the list of groups.

    """
    session = database_connection.get_database_session()
    try:
        group_query = session.query(GroupDB).order_by(GroupDB.id)
        if limit != 0:
            group_query = group_query.limit(limit)
        group_list = group_query.all()

        result = {"groups": {}}

        for index, group_db in enumerate(group_list):
            group = Group(group_db, base_url)
            result["groups"][index] = group

        return result
    except (OperationalError, ProgrammingError, InvalidRequestError, DataError) as e:
        return {"error": str(e), "status": "Database query error"}
    except (TypeError, AttributeError) as e:
        return {"error": str(e), "status": "Error processing group data"}
    finally:
        session.close()


def get_group_by_id(id, base_url: str = "", metadata=False):
    """
    Retrieve a Group by its identifier and return its JSON representation.

    Args:
        id:  (int) Identifier of the group to retrieve.
        base_url : (str) Base URL used to construct item links in the Group representation
        metadata : (bool) If the result must return metadata

    Returns:
        dict JSON-serializable representation of the Group.

    """
    session = database_connection.get_database_session()
    try:
        group_db = session.query(GroupDB).filter(GroupDB.id == id).first()

        if group_db is None:
            raise TypeError("Group Not Found")

        group = Group(group_db, base_url)

        groups_count = session.query(GroupDB).count()
        return group.toJSON(metadata, groups_count)

    except TypeError as e:
        return {"error": str(e), "status": "Not Found a group with this ID"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_random_group(base_url: str = ""):
    """
    Retrieve a random Group and return its JSON representation.

    Args:
        base_url : (str) Base URL used to construct item links in the Group representation

    Returns:
        dict JSON-serializable representation of the Group.

    """
    session = database_connection.get_database_session()
    try:
        group_db = session.query(GroupDB).order_by(func.random()).first()

        group = Group(group_db, base_url)

        return group.toJSON()
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
