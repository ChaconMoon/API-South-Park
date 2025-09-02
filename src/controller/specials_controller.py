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
            special_info = Special(
                id=int(row[0]) if row[0] is not None else 0,
                title=str(row[1]) if row[1] is not None else "",
                release_date=str(row[2]) if row[2] is not None else "",
                description=str(row[3]) if row[3] is not None else "",
                link=str(row[4]) if row[4] is not None else "",
            )
        if add_url:
            result = dict()
            result["name"] = special_info.model_dump()["name"]
            result["url"] = f"{base_url}special/{row[0]}"
            return result
        query_result = get_query_result(text("SELECT * FROM public.specials"))
        result = dict()
        result["special"] = special_info.model_dump()
        result["metadata"] = dict()
        result["metadata"]["total_specials_in_database"] = query_result.rowcount
        return result

    except Exception as e:
        return {"error": str(e), "status": "failed"}
