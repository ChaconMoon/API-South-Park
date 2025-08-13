from sqlalchemy import text
from src.controller.alter_ego_controller import get_all_alteregos_of_a_character
from src.controller.episodes_controller import get_episode_by_id
from src.model.characters import Character
from src.controller.data_controller import parse_array_to_list
from src.controller.database_connection import get_query_result


# Connection with the database
def get_character_by_id(id: int, add_url=False, base_url=""):
    try:
        query_result = get_query_result(
            text("SELECT * FROM public.characters Where id=:id"), {"id": id}
        )

        for row in query_result:
            character = Character(
                id=int(row[0]) if row[0] is not None else 0,
                name=str(row[1]) if row[1] is not None else "",
                friend_group=int(row[2]) if row[2] is not None else 0,
                family=int(row[3]) if row[3] is not None else 0,
                birthday=str(row[4]) if row[4] is not None else "",
                age=int(row[5]) if row[5] is not None else 0,
                religion=parse_array_to_list(row[6]),
                first_apperance=get_episode_by_id(int(row[7])),
                images=parse_array_to_list(row[8], is_url=True, base_url=base_url),
                alter_egos=get_all_alteregos_of_a_character(
                    id, add_url=True, base_url=base_url
                ),
                famious_guest=bool(row[9]) if row[9] is not None else False,
            )
        result = character.model_dump()
        if add_url:
            result["url"] = f"{base_url}character/{row[0]}"
        return result
    except Exception as e:
        return {"error": str(e), "status": "failed"}
