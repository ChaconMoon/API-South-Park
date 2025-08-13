from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.episode import Episode


# Connection with the database
def get_episode_by_id(id: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text("SELECT * FROM public.episodes where id=:id"), {"id": id}
        )

        for row in query_result:
            episode_info = Episode(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                sesaon=str(row[2]) if row[2] is not None else "",
                episode=str(row[3]) if row[3] is not None else "",
                realese_date=str(row[4]) if row[4] is not None else "",
                description=str(row[5]) if row[5] is not None else "",
                view_on_website=str(row[6]) if row[6] is not None else "",
            )
        result = episode_info.model_dump()
        if add_url:
            result["url"] = f"{base_url}episode/{row[0]}"
        return result

    # Si no se encontró el personaje
    # return {"error": "Character not found", "status": "not_found"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}
