"""
Module written by Carlos Chacón.

This module defines the iframe endpoints for the South Park API website.
It provides routes to render template responses for different content sections
like characters, episodes, songs, etc. Currently using static content instead
of dynamic API calls for performance reasons.
"""

from fastapi import APIRouter, Request, Response

from src.controller.structure.web_templates_controller import templates

# Commented imports for dynamic content (currently disabled)
# from src.website_elements.create_character_card_web import create_character_image_grid
# from src.website_elements.create_episode_card_web import create_episode_image_grid
# from src.website_elements.create_song_card_web import create_song_image_grid
# from src.website_elements.create_album_card_web import create_album_image_grid
# from src.website_elements.create_alter_ego_card_web import create_alter_ego_image_grid
# from src.website_elements.create_families_card_web import create_family_image_grid
# from src.website_elements.create_game_card_web import create_game_image_grid
# from src.website_elements.create_specials_card_web import (
#     create_special_image_grid,
# )

router = APIRouter(tags=["Iframes"])


@router.get("/iframe/characters")
def create_characters_iframe(response: Response, request: Request) -> dict:
    """
    Render the characters section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for characters section

    """
    return templates.TemplateResponse(
        "characters.html",
        {
            "request": request,
            # NOW DISABLED
            # "character_cards": create_character_image_grid(
            #    base_url=request.base_url,
            #     ids=[4, 3, 2, 1, 58, 52, 99, 78, 42, 382, 141, 107],
            # ),
        },
    )


@router.get("/iframe/episodes")
def create_episodes_iframe(response: Response, request: Request) -> dict:
    """
    Render the episodes section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for episodes section

    """
    return templates.TemplateResponse(
        "episodes.html",
        {
            "request": request,
            # NOW DISABLED
            # "episode_cards": create_episode_image_grid(
            #    base_url=request.base_url, ids=[1, 263, 325, 303, 200, 117]
            # ),
        },
    )


@router.get("/iframe/songs")
def create_songs_iframe(response: Response, request: Request) -> dict:
    """
    Render the songs section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for songs section

    """
    return templates.TemplateResponse(
        "songs.html",
        {
            "request": request,
            # NOW DISABLED
            # "song_cards": create_song_image_grid(
            #    base_url=request.base_url, ids=[1, 30, 50, 63, 27, 68]
            # ),
        },
    )


@router.get("/iframe/albums")
def create_albums_iframe(response: Response, request: Request) -> dict:
    """
    Render the albums section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for albums section

    """
    return templates.TemplateResponse(
        "albums.html",
        {
            "request": request,
            # NOW DISABLED
            # "album_cards": create_album_image_grid(
            #    base_url=request.base_url, ids=[1, 2, 3, 4, 5, 6]
            # ),
        },
    )


@router.get("/iframe/alter_egos")
def create_alter_egos_iframe(response: Response, request: Request) -> dict:
    """
    Render the alter egos section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for alter egos section

    """
    return templates.TemplateResponse(
        "alter_egos.html",
        {
            "request": request,
            # NOW DISABLED
            # "alter_ego_cards": create_alter_ego_image_grid(
            #    base_url=request.base_url,
            #    ids=[[4, 0, 2, 1], [58, 0, 4, 1], [42, 4, 3, 1]],
            # ),
        },
    )


@router.get("/iframe/families")
def create_fmilies_iframe(response: Response, request: Request) -> dict:
    """
    Render the families section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for families section

    """
    return templates.TemplateResponse(
        "families.html",
        {
            "request": request,
            # NOW DISABLED
            # "families_cards": create_family_image_grid(
            #    base_url=request.base_url, ids=[1, 3, 20, 34, 24, 48]
            # ),
        },
    )


@router.get("/iframe/games")
def create_games_iframe(response: Response, request: Request) -> dict:
    """
    Render the games section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for games section

    """
    return templates.TemplateResponse(
        "games.html",
        {
            "request": request,
            # NOW DISABLED
            # "games_cards": create_game_image_grid(
            #    base_url=request.base_url,
            #    ids=[19, 20, 21, 22, 2, 14, 13, 28, 17, 10, 27, 33],
            # ),
        },
    )


@router.get("/iframe/specials")
def create_specials_iframe(response: Response, request: Request) -> dict:
    """
    Render the specials section iframe template.

    Args:
        response (Response): FastAPI response object
        request (Request): FastAPI request object

    Returns:
        dict: Template response for specials section

    """
    return templates.TemplateResponse(
        "specials.html",
        {
            "request": request,
            # NOW DISABLED
            # "specials_cards": create_special_image_grid(
            #    base_url=request.base_url, ids=[1, 2, 3, 4, 5, 6, 7]
            # ),
        },
    )
