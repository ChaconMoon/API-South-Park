from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.album import Album
from src.controller.songs_controller import get_all_songs_of_a_album


# Connection with the database
def get_album_by_id(id: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text("""
                SELECT * FROM public.albums where id = :id"""),
            {"id": id},
        )

        for row in query_result:
            cover_url = str(row[3]) if row[3] is not None else ""
            album = Album(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                release_date=str(row[2]) if row[2] is not None else None,
                album_cover=base_url + cover_url,
                songs=get_all_songs_of_a_album(int(row[0]), base_url, add_url=True),
            )
        return album.model_dump()

        # Si no se encontró el personaje
        # return {"error": "Character not found", "status": "not_found"}

    except Exception as e:
        return {"error": str(e), "status": base_url}
