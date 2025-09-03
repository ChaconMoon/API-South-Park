from fastapi import FastAPI
from fastapi import Request, Response, status
from fastapi.staticfiles import StaticFiles
import uvicorn
from src.controller.alter_ego_controller import (
    get_alter_ego_by_character_and_id,
    get_all_alteregos_of_a_character,
)
from src.controller.database_status import get_database_status
from src.controller.family_controller import get_family_by_id
from src.controller.character_controller import get_character_by_id
from src.controller.episodes_controller import get_episode_by_id
from src.controller.specials_controller import get_special_by_id
from src.controller.songs_controller import get_song_by_id
from src.controller.album_controller import get_album_by_id

app = FastAPI()

app.mount("/img", StaticFiles(directory="img"), name="img")


@app.get("/")
def index(response: Response):
    json = get_database_status()

    if "error" in json:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


@app.get("/album/{id}")
def show_album(id: int, request: Request, response: Response):
    base_url = str(request.base_url)
    json = get_album_by_id(id, base_url=base_url)
    if "error" in json:
        if json["error"] == "Album not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "album" in json:
        response.status_code == status.HTTP_200_OK
    return json


@app.get("/song/{id}")
def show_song(id: int, request: Request, response: Response):
    base_url = str(request.base_url)
    json = get_song_by_id(id, base_url=base_url)
    if "error" in json:
        if json["error"] == "Song not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "song" in json:
        response.status_code = status.HTTP_200_OK
    return json


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
