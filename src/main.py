"""
Module written by Carlos Chacón

This Module contain the main class of the API and create de endpoints used by the API
"""

# Import of FastAPI.
import json
from fastapi import FastAPI, HTTPException
from fastapi import Request, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import the uvicorn library.
from markdown import markdown
import uvicorn

# Internal inputs.
from src.controller.date_controller import get_today_birthday_character
from src.controller.easter_egg_controller import get_easter_egg
from src.website_elements.create_character_card_web import create_character_image_grid
from src.website_elements.create_episode_card_web import create_episode_image_grid
from src.website_elements.create_song_card_web import create_song_image_grid
from src.website_elements.create_album_card_web import create_album_image_grid
from src.website_elements.create_alter_ego_card_web import create_alter_ego_image_grid
from src.website_elements.create_families_card_web import create_family_image_grid
from src.website_elements.create_game_card_web import create_game_image_grid
from src.website_elements.create_specials_card_web import (
    create_special_image_grid,
)
from src.website_elements.create_post_card_grid import (
    create_post_grid_in_blog,
    create_blog_links,
    get_blog_last_index,
    get_intro_in_menu,
    get_social_media_thumbnail_in_menu,
    get_title_in_menu,
)
from src.website_elements.create_404_iamge_web import get_404_image

from src.controller.alter_ego_controller import (
    get_alter_ego_by_character_and_id,
    get_all_alteregos_of_a_character,
)
from src.controller.chinpokomon_controller import get_chinpokomon_by_id
from src.controller.database_status import get_database_status
from src.controller.family_controller import get_family_by_id
from src.controller.character_controller import (
    get_character_by_id,
    get_characters_by_search,
)
from src.controller.episodes_controller import get_episode_by_id, get_last_episode
from src.controller.specials_controller import get_special_by_id
from src.controller.songs_controller import get_song_by_id
from src.controller.album_controller import get_album_by_id
from src.controller.game_controller import get_game_by_id
from src.website_elements.create_footer_web import create_footer


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

app.mount(
    "/blog/images/",
    StaticFiles(directory="website/posts/thumbnails"),
    name="posts_images",
)

app.mount(
    "/blog/social_media/images/",
    StaticFiles(directory="website/posts/social_media_thumbnails"),
    name="social_media_images",
)
app.mount("/blog/posts/", StaticFiles(directory="website/posts"), name="posts")
# Mount the img directory with the images of the database.
app.mount("/img", StaticFiles(directory="img"), name="img")

app.mount("/styles", StaticFiles(directory="styles"), name="styles")

app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")

app.mount("/javascript", StaticFiles(directory="javascript"), name="javascript")


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    path = request.url.path

    if path.startswith("/api/"):
        return JSONResponse(status_code=404, content={"error": "Not Found"})

    else:
        return templates.TemplateResponse(
            "404.html",
            context={
                "request": request,
                "image_404": f'<img id="Not_Found_Image" src="{get_404_image()}">',
                "footer": create_footer(),
            },
        )


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
            "games_cards": create_game_image_grid(
                base_url=request.base_url,
                ids=[19, 20, 21, 22, 2, 14, 13, 28, 17, 10, 27, 33],
            ),
            "specials_cards": create_special_image_grid(
                base_url=request.base_url, ids=[1, 2, 3, 4, 5, 6, 7]
            ),
            "example_api_response": json.dumps(
                get_character_by_id(100, base_url=str(request.base_url)),
                indent=4,
                ensure_ascii=False,
            ),
            "footer": create_footer(),
        },
    )


#
# EXPERIMENTAL
#


@app.get("/api/search/characters/{search_param}", tags=["EXPERIMENTAL"])
def search_character(
    response: Response,
    request: Request,
    search_param: str,
    metadata: bool = False,
    limit: int = 10,
) -> dict:
    """
    TESTING SEARCH IN API.
    """
    json = get_characters_by_search(
        search_param=search_param,
        add_url=False,
        metadata=False,
        base_url=str(request.base_url),
        limit=limit,
    )
    if "error" in json:
        if json["error"] == "Character not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_200_OK
    return json


@app.get("/blog/article/{entry}", tags="Blog")
def show_blog(request: Request, response: Response, entry: str):
    try:
        with open(f"./website/posts/{entry}.MD", encoding="utf-8") as f:
            markdown_content = f.read()
        html_blog_entry = markdown(
            markdown_content,
            extensions=["fenced_code", "tables", "attr_list", "md_in_html"],
        )
        html_blog_entry = html_blog_entry.replace("<p><img", "<img")
        html_blog_entry = html_blog_entry.replace('webp" /></p>', 'webp" />')
    except FileNotFoundError as e:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse(
        "blog_page_post.html",
        context={
            "request": request,
            "blog_item": html_blog_entry,
            "base_url": request.base_url,
            "articule_title_in_social_media": get_title_in_menu(f"{entry}.MD"),
            "articule_description_in_social_media": get_intro_in_menu(f"{entry}.MD"),
            "image_in_social_media": f"{str(request.base_url)[:-1].replace('http://', 'https://')}{get_social_media_thumbnail_in_menu(f'{entry}.MD')}",
            "url_in_social_media": f"{str(request.base_url).replace('http://', 'https://')}blog/article/{entry}",
            "footer": create_footer(),
        },
    )


@app.get("/blog/{index}", tags="blog")
def show_posts_grid(request: Request, response: Response, index: int):
    grid_elements = create_post_grid_in_blog(
        start_index=index, base_url=request.base_url
    )
    print(grid_elements)
    if grid_elements != "":
        return templates.TemplateResponse(
            "blog_page.html",
            context={
                "request": request,
                "base_url": request.base_url,
                "blog_posts_grid": grid_elements,
                "blog_links": create_blog_links(),
                "footer": create_footer(),
            },
        )
    else:
        return RedirectResponse(f"/blog/{get_blog_last_index()}")


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


# Create the endpoint to get the albums.
@app.get("/api/albums/{id}", tags=["Music"])
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


# Create the endpoint to get the songs.
@app.get("/api/songs/{id}", tags=["Music"])
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


# Create the endpoint to get the special episodes.
@app.get("/api/specials/{id}", tags=["TV Show"])
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


# Create the endpoint to get the families.
@app.get("/api/families/{id}", tags=["Characters"])
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


# Create the endpoint to get the characters.
@app.get("/api/characters/{id}", tags=["Characters"])
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
    else:
        response.status_code = status.HTTP_200_OK
    return json


# Create the endpoint to get the episodes.
@app.get("/api/episodes/{id}", tags=["TV Show"])
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


# Create the endpoint to get one alter ego of a character.
@app.get("/api/characters/{id}/alteregos/{alter_id}", tags=["Characters"])
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


# Create the endpoint to get all the alteregos of a character.
@app.get("/api/characters/{id}/alteregos", tags=["Characters"])
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


# Create the endpoint to get all the alteregos of a character.
@app.get("/api/games/{id}/", tags=["Games"])
def show_game(
    id: int, request: Request, response: Response, metadata: bool = False
) -> dict:
    """
    Get the response with the all the alteregos of one specific character.

    Returns:
    A dict with the response
    """
    base_url = str(request.base_url)
    json = get_game_by_id(id=id, base_url=base_url, metadata=metadata)
    if json is None:
        json = {"error": "Game not found", "status": "failed"}
    if "error" in json:
        if json["error"] == "Game not found":
            response.status_code = status.HTTP_404_NOT_FOUND
        elif json["error"] == "Database not avalible":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif "alteregos" in json:
            response.status_code = status.HTTP_200_OK
    return json


@app.get("/api/todaybirthdays")
def get_characters_with_birthday_today(request: Request):
    return get_today_birthday_character(base_url=str(request.base_url))


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
