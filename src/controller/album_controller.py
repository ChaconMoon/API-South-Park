"""
Module written by Carlos Chacón.

This module get the param of the API in the get album operations, make the query to the API and return the result.
"""

# Import SQLAlquemy to make the query
from sqlalchemy import text

# Internal inputs
from src.controller.database_connection import get_query_result
from src.model.album import Album
from src.controller.songs_controller import get_all_songs_of_a_album


# Get album by this id
def get_album_by_id(id: int, add_url=False, base_url="", metadata=False) -> dict:
    """
    Get the ID of a album and returns a dict with the content of this album in the database.

    Params:
        id (int): The id of the album in the database.
        add_url (bool): Define is the query must return the URL.
        base_url (str): The url used to create the URL API.
    Returns:
        A dict with the response or a dict with the error.
    """
    try:
        # Make the query to the Database
        query_result = get_query_result(
            text("""
                SELECT * FROM public.albums where id = :id"""),
            {"id": id},
        )

        # If the is a error in the query returns the error
        if query_result is None:
            return {"error": "Database not avalible", "status": "failed"}
        if query_result.rowcount == 0:
            return {"error": "Album not found", "status": "failed"}

        # Create a objet with the result of the query
        for row in query_result:
            cover_url = str(row[3]) if row[3] is not None else ""
            album = Album(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                release_date=str(row[2]) if row[2] is not None else None,
                album_cover=base_url + cover_url,
                songs=get_all_songs_of_a_album(int(row[0]), base_url, add_url=True),
                album_url=str(row[4]) if row[4] is not None else "",
            )

        # Create the object with the URL
        if add_url:
            result = dict()
            result["name"] = album["name"]
            result["url"] = f"{base_url}api/album/{album['id']}"
            return result

        # Create the complete object with the metadata
        query_result = get_query_result(text("SELECT * FROM public.albums"))
        result = dict()
        if not metadata:
            result = album.model_dump()
        else:
            result["album"] = album.model_dump()
            result["metadata"] = dict()
            result["metadata"]["total_albums_in_database"] = query_result.rowcount
        return result

    # Control exceptions
    except TypeError as e:
        return {"error": str(e), "status": "failed"}
