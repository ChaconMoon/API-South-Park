"""
Module written by Carlos Chacón

This Module contain the main class of the API and create de operations used by the API
"""

# Import of FastAPI.
import json
from fastapi import FastAPI
from fastapi import Request, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import the uvicorn library.
import uvicorn

# Internal inputs.
from src.controller.easter_egg_controller import get_easter_egg
from src.website_elements.create_character_card_web import create_character_image_grid
from src.website_elements.create_episode_card_web import create_episode_image_grid
from src.website_elements.create_song_card_web import create_song_image_grid
from src.website_elements.create_album_card_web import create_album_image_grid
from src.website_elements.create_alter_ego_card_web import create_alter_ego_image_grid
from src.website_elements.create_families_card_web import create_family_image_grid
from src.controller.alter_ego_controller import (
    get_alter_ego_by_character_and_id,
    get_all_alteregos_of_a_character,
)
from src.controller.chinpokomon_controller import get_chinpokomon_by_id
from src.controller.database_status import get_database_status
from src.controller.family_controller import get_family_by_id
from src.controller.character_controller import get_character_by_id
from src.controller.episodes_controller import get_episode_by_id, get_last_episode
from src.controller.specials_controller import get_special_by_id
from src.controller.songs_controller import get_song_by_id
from src.controller.album_controller import get_album_by_id


# Create the description of de API

description = """
The South Park API allows you to search all the info that you need about the universe of South Park

## Items.

You can search information about:

The songs of the Albums of the show: **85 records** __(Updated at: 15/09/2025 [South Park The 25th Anniversary Concert])__

The albums of the show: **6 records** __(Updated at: 15/09/2025 [South Park The 25th Anniversary Concert])__

The characters of the TV Show: **410 records** __(Updated at: 15/09/2025 [Table in progress])__

The alter egos of the characters of the show: **100 records** __(Updated at: 15/09/2025 [Missing: Dougie / General Disarray and Mr. Slave])__

The episodes of the show: **325 records** __(Updated at: 15/09/2025 [Wok is Dead S27E04])__

The families of the show: **61 records** __(Updated at: 15/09/2025 [Table in progress])__

The South Park games / videogames: **33 records** __(Updated at: 15/09/2025 [South Park: Snow Day])__

The Paramount + specials: **7 records** __(Update at: 15/09/2025 [They won't make more specials, database table finished])__
"""

api_tags = [
    {"name": "Heath_Check", "description": "Get the status of the database"},
    {
        "name": "Characters",
        "description": "Get data about the characters and their families",
    },
    {"name": "Episodes", "description": "Get data about the episodes of the TV show"},
    {
        "name": "Music",
        "description": "Get data about the albums and songs and they URL to listen it.",
    },
    {"name": "Other", "description": "Data of other items"},
]
# Create the FastAPI app.
app = FastAPI(
    title="South Park API",
    description=description,
    summary="All the info that you need about South Park in one place",
    version="0.1 public beta",
    contact={
        "name": "Carlos Chacón",
        "url": "https://twitter.com/chaconmoon_dev",
        "email": "carloschaconmolina@gmail.com",
    },
    license_info={"name": "GPL 3.0", "url": "https://www.gnu.org/licenses/gpl-3.0"},
    redoc_url="/api/redoc",
    docs_url="/api/docs",
)


# Create Jinja templates directory

templates = Jinja2Templates(directory="templates")


# Mount the img directory with the images of the database.
app.mount("/img", StaticFiles(directory="img"), name="img")

app.mount("/styles", StaticFiles(directory="styles"), name="styles")

app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")

app.mount("/javascript", StaticFiles(directory="javascript"), name="javascript")


# Create the basic response of the API with the connection of the API.
@app.get("/")
def index(response: Response, request: Request) -> dict:
    """
    Get the response with the connection of the API.

    Returns:
    A dict with the response.
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "base_url": request.base_url,
            "character_cards": create_character_image_grid(
                base_url=request.base_url,
                ids=[4, 3, 2, 1, 58, 52, 99, 78, 42, 382, 141, 107],
            ),
            "episode_cards": create_episode_image_grid(
                base_url=request.base_url, ids=[1, 263, 325, 303, 200, 117]
            ),
            "song_cards": create_song_image_grid(
                base_url=request.base_url, ids=[1, 30, 50, 63, 27, 68]
            ),
            "album_cards": create_album_image_grid(
                base_url=request.base_url, ids=[1, 2, 3, 4, 5, 6]
            ),
            "alter_ego_cards": create_alter_ego_image_grid(
                base_url=request.base_url,
                ids=[[4, 0, 2, 1], [58, 0, 4, 1], [42, 4, 3, 1]],
            ),
            "families_cards": create_family_image_grid(
                base_url=request.base_url, ids=[1, 3, 20, 34, 24, 48]
            ),
            "example_api_response": json.dumps(
                get_character_by_id(100, base_url=str(request.base_url)),
                indent=4,
                ensure_ascii=False,
            ),
        },
    )


# Create the basic response of the API with the connection of the API.
@app.get("/api/", tags=["Health Check"])
def api_index(response: Response) -> dict:
    """
    Get the response with the connection of the API.

    Returns:
    A dict with the response.
    """
    json = get_database_status()

    if "error" in json:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get the albums.
@app.get("/api/album/{id}", tags=["Music"])
def show_album(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the album with a specific id.

    Returns:
    A dict with the response.
    """
    base_url = str(request.base_url)
    json = get_album_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Album not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        if json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "album" in json:
        response.status_code == status.HTTP_200_OK
    return json


# Create the operation to get the songs.
@app.get("/api/song/{id}", tags=["Music"])
def show_song(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the song with a specific id.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_song_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Song not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "song" in json:
        response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get the special episodes.
@app.get("/api/special/{id}", tags=["TV Show"])
def show_special(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the special with a specific id.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_special_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Special not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    elif "special" in json:
        response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get the families.
@app.get("/api/family/{id}", tags=["Characters"])
def show_family(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the family with a specific id.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_family_by_id(id, url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Family not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "family" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get the characters.
@app.get("/api/character/{id}", tags=["Characters"])
async def show_character(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the character with a specific id.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_character_by_id(id, base_url=base_url, metadata=metadata)
    if "error" in json:
        if json["error"] == "Character not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "character" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get the episodes.
@app.get("/api/episode/{id}", tags=["TV Show"])
def show_episode(
    id: int, response: Response, request: Request, metadata: bool = False
) -> dict:
    """
    Get the response with the episode with a specific id.

    Returns:
    A dict with the response
    """
    json = get_episode_by_id(id, base_url=str(request.base_url), metadata=metadata)
    if "error" in json:
        if json["error"] == "Episode not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "episode" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get one alter ego of a character.
@app.get("/api/character/{id}/alterego/{alter_id}", tags=["Characters"])
def show_alterergo(
    id: int, alter_id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the alterego of one espefic ID of one specific character.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_alter_ego_by_character_and_id(
        id_character=id, id_alter_ego=alter_id, base_url=base_url, metadata=metadata
    )
    if "error" in json:
        if json["error"] == "Alter Ego not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alterego" in json:
            response.status_code = status.HTTP_200_OK
    return json


# Create the operation to get all the alteregos of a character.
@app.get("/api/character/{id}/alteregos", tags=["Characters"])
def show_all_alteregos(id: int, request: Request, response: Response) -> dict:
    """
    Get the response with the all the alteregos of one specific character.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_all_alteregos_of_a_character(id_character=id, base_url=base_url)
    if json is None:
        json = {"error": "Alter Egos not found", "status": "failed"}
    if "error" in json:
        if json["error"] == "Alter Egos not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alteregos" in json:
            response.status_code = status.HTTP_200_OK
    return json


@app.get("/api/lastepisode", tags=["TV Show"])
def get_the_last_episode():
    """
    Returns the last episode of the serie.

    Returns:
    A dict with the response
    """
    return get_last_episode()


@app.get("/api/chinpokomon/{id}", tags=["Others"])
def get_chinpokomon(id: int, request: Request, response: Response):
    base_url = str(request.base_url)
    return get_chinpokomon_by_id(id=id, base_url=base_url)


@app.get("/api/easteregg/{name}", tags=["Others"])
def return_easter_egg(name: str, request: Request, response: Response):
    base_url = str(request.base_url)
    return get_easter_egg(name=name, base_url=base_url)


# Start the API execution.
if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
