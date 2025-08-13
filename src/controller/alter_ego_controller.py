from sqlalchemy import text
from src.controller.database_connection import get_query_result
from src.model.alter_ego import AlterEgo
from src.controller.data_controller import parse_array_to_list


# Connection with the database
def get_alter_ego_by_character_and_id(
    id_alter_ego: int, id_character: int, add_url=False, base_url=""
):
    try:
        query_result = get_query_result(
            text("""
                        SELECT alter_ego.id,characters.name,alter_ego.name as alter_ego, alter_ego.images FROM public.alter_ego, public.characters
                        where characters.id = alter_ego.original_character and characters.id = :id_character AND alter_ego.id = :id_alter_ego"""),
            {"id_character": id_character, "id_alter_ego": id_alter_ego},
        )

        for row in query_result:
            alter_ego = AlterEgo(
                id=int(row[0]) if row[0] is not None else 0,
                original_character=str(row[1]) if row[1] is not None else "",
                name=str(row[2]) if row[2] is not None else "",
                images=parse_array_to_list(row[3], is_url=True, base_url=base_url),
            )
        if add_url:
            result = alter_ego.model_dump()
            result["url"] = (
                f"{base_url}characters/{id_character}/alterego/{id_alter_ego}"
            )
            return result
        return alter_ego.model_dump()

        # Si no se encontró el personaje
        # return {"error": "Character not found", "status": "not_found"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}


def get_all_alteregos_of_a_character(id_character: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text(
                """SELECT * FROM public.alter_ego where original_character = :id_character order by id asc"""
            ),
            {"id_character": id_character},
        )
        number_of_alter_egos = query_result.rowcount
        if number_of_alter_egos == 0:
            return {}
        alter_ego_id = 1
        result = dict()
        while alter_ego_id != number_of_alter_egos:
            result[alter_ego_id - 1] = get_alter_ego_by_character_and_id(
                id_alter_ego=alter_ego_id, id_character=id_character, base_url=base_url
            )
            alter_ego_id += 1
        return result
    except Exception:
        return {"message": "error"}
