"""
Module written by Carlos Chacón.

This module get the param of the API in the get album operations,
make the query to the API and return the result.
"""

# Import SQLAlquemy to make the query
from sqlalchemy import func
from sqlalchemy.exc import OperationalError

# Internal inputs
from src.controller import database_connection
from src.model.album import Album
from src.model.ORM.album_db import AlbumDB


def get_album_list_by_search(base_url="", search_param="", limit: int = 0):
    """
    Search for albums by name using a partial, case-insensitive match.

    Args:
        base_url (str): The base URL for generating resource URLs.
        search_param (str): The search term to match against album names.
        limit (int): The maximum number of albums to return. If 0, no limit.

    Returns:
        dict: A dictionary containing the list of matching albums.

    """
    session = database_connection.get_database_session()
    try:
        album_query = session.query(AlbumDB).filter(
            AlbumDB.name.ilike(f"%{search_param}%")
        )
        if limit != 0:
            album_query = album_query.limit(limit)
        album_db_list = album_query.all()
        result = dict()
        result = {"albums": {}}
        for index, album_db in enumerate(album_db_list):
            album = Album(album_db, base_url)
            result["albums"][index] = album.toJSON()
        if result == {"albums": {}}:
            raise TypeError("Album Not Found")
        return result
    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_album_list(base_url="", limit: int = 0):
    """
    Get a list of all albums.

    Args:
        base_url (str): The base URL for generating resource URLs.
        limit (int): The maximum number of albums to return. If 0, no limit.

    Returns:
        dict: A dictionary containing the list of albums.

    """
    session = database_connection.get_database_session()
    try:
        album_query = session.query(AlbumDB)
        if limit != 0:
            album_query = album_query.limit(limit)
        album_db_list = album_query.all()
        result = dict()
        result = {"albums": {}}
        for index, album_db in enumerate(album_db_list):
            album = Album(album_db, base_url)
            result["albums"][index] = album.toJSON()
        if result == {"albums": {}}:
            raise TypeError("Album Not Found")
        return result
    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_album(base_url="", exclude_not_available: bool = False):
    """
    Return a dict with the content of a random album.

    Params:
        base_url (str): The url used to create the URL API.
        exclude_not_available (bool): If true excludes the not available albums.

    Returns:
        A dict with the response or a dict with the error.

    """
    session = database_connection.get_database_session()
    try:
        album_query = session.query(AlbumDB)
        if exclude_not_available:
            album_query = album_query.filter(AlbumDB.album_url != "NOT AVAILABLE")
        album_db = album_query.order_by(func.random()).first()
        if album_db is None:
            raise TypeError("Album Not Found")
        album = Album(album_db, base_url)
        return album.toJSON()
    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


# Get album by this id
def get_album_by_id(id: int, add_url=False, base_url="", metadata=False) -> dict:
    """
    Get the ID of a album and returns a dict with the content of this album.

    Params:
        id (int): The id of the album in the database.
        add_url (bool): Define is the query must return the URL.
        base_url (str): The url used to create the URL API.

    Returns:
        A dict with the response or a dict with the error.

    """
    session = database_connection.get_database_session()
    try:
        album_db = session.query(AlbumDB).filter(AlbumDB.id == id).first()
        if album_db is None:
            raise TypeError("Album Not Found")
        album = Album(album_db, base_url)
        album_count = session.query(AlbumDB).count()
        return album.toJSON(metadata, album_count)
    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
