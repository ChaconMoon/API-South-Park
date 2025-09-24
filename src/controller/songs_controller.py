"""
Module written by Carlos Chacón.

This module get the param of the API in the get song operations, make the query to the API and return the result.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Internal Imports
from src.controller.database_connection import get_query_result
from src.model.song import Song


# Get all the songs of the same album
def get_all_songs_of_a_album(id: int, base_url="", add_url=False) -> dict:
    """
    Return a dict with all the songs of a specific album.

    Params:
        id (int): The ID of the album.
        base_url (str): The base URL to create the reference URL.
        add_url (bool): If the result must contain the URL.
    Returns:
        A dict with all the songs of the album.
    """
    # Create the object to store the result
    result = dict()
    try:
        # Make the query to the database.
        query_result = get_query_result(
            text("""
                        SELECT * FROM public.album_songs where album = :id order by id asc"""),
            {"id": id},
        )
        song_number = 1

        # Create the response to the API and return it.
        for row in query_result:
            lyrics = str(row[3]) if row[3] is not None else ""
            song = Song(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                album_number=int(row[2]) if row[2] is not None else None,
                lyrics=lyrics,
                song_url=str(row[4]) if row[4] is not None else "",
            )
            if add_url:
                result[song_number] = dict()
                result[song_number]["name"] = song.model_dump()["name"]
                result[song_number]["url"] = (
                    f"{base_url}api/song/{song.model_dump()['id']}"
                )
            song_number += 1
        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}


# Get one song data
def get_song_by_id(id: int, add_url=False, base_url=""):
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
    try:
        # Make the query to the Database
        query_result = get_query_result(
            text("""
                SELECT * FROM public.album_songs where id = :id"""),
            {"id": id},
        )
        # If the is a error in the query returns the error
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        elif query_result.rowcount == 0:
            return {"error": "Song not found", "status": "failed"}

        # Create a objet with the result of the query
        for row in query_result:
            # Replace literal \n with actual newlines in lyrics
            lyrics = str(row[3]) if row[3] is not None else ""

            song = Song(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                album_number=int(row[2]) if row[2] is not None else None,
                lyrics=lyrics,
                song_url=str(row[4]) if row[4] is not None else "",
            )
        query_result = get_query_result(text("SELECT * FROM public.album_songs"))
        result = dict()
        result["song"] = song.model_dump()
        result["metadata"] = dict()
        result["metadata"]["total_songs_in_database"] = query_result.rowcount
        return result

    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
