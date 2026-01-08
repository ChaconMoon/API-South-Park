"""
Module written by Carlos Chacón.

This module configures and initializes the FastAPI application for the South Park API.
It sets up routing, static file serving, error handling, and API documentation.

The API provides comprehensive data about the South Park universe including:
- Characters and their alter egos
- Episodes and specials
- Music albums and songs
- Video games
- Family relationships
- Chinpokomon creatures

All data is served through RESTful endpoints with proper documentation
and consistent error handling.
"""

# Create the FastAPI app.
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.controller.characters import characters_endpoints
from src.controller.chinpokomon import chinpokomon_endpoints
from src.controller.games import games_endpoint
from src.controller.handlers.not_found_handler import custom_404_handler
from src.controller.iframes import iframes_endpoints
from src.controller.music import music_endpoints
from src.controller.others import easter_egg_endpoint
from src.controller.others import miscellaneous_endpoints
from src.controller.structure import (
    blog_endpoints,
    health_check_endpoints,
    web_endpoints,
)
from src.controller.tvshow import tv_show_endpoints

# API Description - Lists available data and update status
description = """
The South Park API allows you to search all the info that you need about the universe of South Park

## Items

You can search information about:

The songs of the Albums of the show: **85 records**
__(Updated at: 15/09/2025 [South Park The 25th Anniversary Concert])__

The albums of the show: **6 records** __(Updated at: 15/09/2025 [South Park The 25th Anniversary Concert])__

The characters of the TV Show: **542 records** __(Updated at: 04/11/2025 [Table in progress])__

The alter egos of the characters of the show: **100 records** __(Updated at: 15/09/2025 [Missing: Dougie / General Disarray and Mr. Slave])__

The episodes of the show: **328 records** __(Updated at: 04/11/2025 [The Woman In The Hat S28E02])__

The families of the show: **67 records** __(Updated at: 04/11/2025 [Table in progress])__

The South Park games / videogames: **33 records** __(Updated at: 15/09/2025 [South Park: Snow Day])__

The Paramount + specials: **7 records** __(Update at: 15/09/2025 [They won't make more specials, database table finished])__
"""  # noqa: E501

# API Tags - Define and document endpoint categories
api_tags = [
    {"name": "Health Check", "description": "Get the status of the database"},
    {
        "name": "Characters",
        "description": "Get data about the characters and their families",
    },
    {"name": "TV Show", "description": "Get data about the episodes of the TV show"},
    {
        "name": "Music",
        "description": "Get data about the albums and songs and they URL to listen it.",
    },
    {"name": "Others", "description": "Data of other items"},
    {"name": "Iframes", "description": "Generates the iframes of the index"},
    {"name": "Web", "description": "Endpoints of the web"},
    {"name": "Blog", "description": "Endpoints of the DevBlog"},
]

# Initialize FastAPI application with metadata
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
    openapi_tags=api_tags,
)

# Register all route handlers
app.include_router(characters_endpoints.router)
app.include_router(iframes_endpoints.router)
app.include_router(web_endpoints.router)
app.include_router(blog_endpoints.router)
app.include_router(chinpokomon_endpoints.router)
app.include_router(games_endpoint.router)
app.include_router(music_endpoints.router)
app.include_router(easter_egg_endpoint.router)
app.include_router(health_check_endpoints.router)
app.include_router(tv_show_endpoints.router)
app.include_router(miscellaneous_endpoints.router)

# Configure custom 404 handler
app.add_exception_handler(404, custom_404_handler)

# Mount static file directories
# Blog related files
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

app.mount(
    "/changeblog/posts/",
    StaticFiles(directory="docs/changelog_posts/"),
    name="changeblog",
)

# Asset directories
app.mount("/img", StaticFiles(directory="img"), name="img")
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/javascript", StaticFiles(directory="javascript"), name="javascript")
