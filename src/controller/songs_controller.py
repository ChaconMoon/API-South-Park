from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.song import Song


# Connection with the database
def get_song_by_id(id: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text("""
                SELECT * FROM public.album_songs where id = :id"""),
            {"id": id},
        )

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
        return song.model_dump()

        # Si no se encontró el personaje
        # return {"error": "Character not found", "status": "not_found"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}
