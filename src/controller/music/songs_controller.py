"""
Module written by Carlos Chacón.

This module get the param of the API in the get song operations,
make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from src.controller import database_connection

# Internal Imports
from src.model.ORM.album_songs_db import AlbumSongDB
from src.model.song import Song


# Get one song data
def get_song_by_id(id: int, add_url=False, base_url="", metadata=False):
    """
    Return a dict a song.

    Params:
        id (int): The ID of the song.
        base_url (str): The base URL to create the reference URL.
        add_url (bool): If the result must contain the URL.

    Returns:
        A dict with all the songs of the album.

    """
    # Get the query result
    session = database_connection.get_database_session()
    try:
        song_db = session.query(AlbumSongDB).filter(AlbumSongDB.id == id).first()
        if song_db is None:
            raise TypeError("Song Not Found")
        song = Song(song_db, base_url)
        return song.toJSON()

    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_song(exclude_not_available: bool = False, base_url="") -> dict:
    """
    Get a specific random song from south park's albums.

    Args:
        base_url (str): The URL used to create the URL from the response.
        exclude_not_available (boolean): If True excludes the not available songs.

    Returns:
        dict: JSON response containing either:
            - Song data if found
            - Error message if not found or database error

    """
    session = database_connection.get_database_session()
    try:
        song_query = session.query(AlbumSongDB)

        if exclude_not_available:
            song_query = song_query.filter(
                AlbumSongDB.song_url != "[NOT AVAILABLE IN STREAMING SERVICES]"
            )
        song_db = song_query.order_by(func.random()).first()
        song = Song(song_db, base_url)
        return song.toJSON()

    except TypeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
