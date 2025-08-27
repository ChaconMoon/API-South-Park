from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from src.controller.alter_ego_controller import (
    get_alter_ego_by_character_and_id,
    get_all_alteregos_of_a_character,
)
from src.controller.database_test import test_database
from src.controller.family_controller import get_family_by_id
from src.controller.character_controller import get_character_by_id
from src.controller.episodes_controller import get_episode_by_id
from src.controller.specials_controller import get_special_by_id
from src.controller.songs_controller import get_song_by_id

app = FastAPI()

app.mount("/img", StaticFiles(directory="img"), name="img")


@app.get("/")
def index():
    return test_database()


@app.get("/song/{id}")
def show_song(id: int, request: Request):
    base_url = str(request.base_url)
    return get_song_by_id(id, base_url=base_url)


@app.get("/special/{id}")
def show_special(id: int, request: Request):
    base_url = str(request.base_url)
    return get_special_by_id(id, base_url=base_url)


@app.get("/family/{id}")
def show_family(id: int, request: Request):
    base_url = str(request.base_url)
    return get_family_by_id(id, url=base_url)


@app.get("/character/{id}")
def show_character(id: int, request: Request):
    base_url = str(request.base_url)
    return get_character_by_id(id, base_url=base_url)


@app.get("/episode/{id}")
def show_episode(id: int):
    return get_episode_by_id(id)


@app.get("/character/{id}/alterego/{alter_id}")
def show_alterergo(id: int, alter_id: int, request: Request):
    base_url = str(request.base_url)
    return get_alter_ego_by_character_and_id(
        id_character=id, id_alter_ego=alter_id, base_url=base_url
    )


@app.get("/character/{id}/alteregos")
def show_all_alteregos(id: int, request: Request):
    base_url = str(request.base_url)
    return get_all_alteregos_of_a_character(id_character=id, base_url=base_url)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
