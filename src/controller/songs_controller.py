from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.song import Song


# Connection with the database
def get_all_songs_of_a_album(id: int, base_url="", add_url=False):
    result = dict()
    try:
        query_result = get_query_result(
            text("""
                        SELECT * FROM public.album_songs where album = :id order by id asc"""),
            {"id": id},
        )
        song_number = 1

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
            if add_url:
                result[song_number] = dict()
                result[song_number]["name"] = song.model_dump()["name"]
                result[song_number]["url"] = f"{base_url}song/{song.model_dump()['id']}"
            song_number += 1
        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}


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

    except Exception as e:
        return {"error": str(e), "status": "failed"}
