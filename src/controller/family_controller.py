from sqlalchemy import text
from src.controller.character_controller import get_character_by_id
from src.controller.database_connection import get_query_result
from src.model.family import Family


# Connection with the database
def get_family_by_id(id: int, url=""):
    result = dict()
    family_members = []
    try:
        query_result = get_query_result(
            text("""SELECT characters.id,characters.name,families.name FROM public.characters,public.families
                                        Where characters.family = families.id And families.id = :id order by characters.id asc"""),
            {"id": id},
        )
        rows = query_result.fetchall()
        for row in rows:
            family_members.append(
                get_character_by_id(int(row[0]), add_url=True, base_url=url)
            )
        family = Family(id=id, name=str(rows[0][2]), images=[])
        result["id"] = family.id
        result["family"] = family.name
        result["members"] = family_members

        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}
