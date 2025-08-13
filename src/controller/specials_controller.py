from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.specials import Special


# Connection with the database
def get_special_by_id(id: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text("""
                SELECT id,title,release_date,description,link FROM public.specials
                where id = :id"""),
            {"id": id},
        )

        for row in query_result:
            episode_info = Special(
                id=int(row[0]) if row[0] is not None else 0,
                title=str(row[1]) if row[1] is not None else "",
                release_date=str(row[2]) if row[2] is not None else "",
                description=str(row[3]) if row[3] is not None else "",
                link=str(row[4]) if row[4] is not None else "",
            )
        if add_url:
            result = episode_info.model_dump()
            result["url"] = f"{base_url}special/{row[0]}"
            return result
        return episode_info.model_dump()

        # Si no se encontró el personaje
        # return {"error": "Character not found", "status": "not_found"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}
