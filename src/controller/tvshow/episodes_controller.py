"""
Module written by Carlos Chacón.

This module handles the database operations for retrieving South Park episodes.
It provides functions to fetch specific episodes by ID and get the latest episode
from the database.
"""

import io

from fastapi.responses import StreamingResponse
from PIL import Image
from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from src.controller import database_connection
from src.model.episode import Episode
from src.model.ORM.episode_db import EpisodeDB


def get_episode_images_by_id_(
    episode_id: int, image_id: int, size: str
) -> StreamingResponse:
    """
    Retrieve a specific image for a South Park episode by episode ID and image ID.

    Args:
        episode_id (int): The ID of the episode.
        image_id (int): The ID of the image.
        size (str): The desired size of the image
          ("original", "large", "medium", "small").

    Returns:
        StreamingResponse: The image file as a streaming response.

    """
    sizes = {"large": (1280, 720), "medium": (960, 540), "small": (640, 480)}
    session = database_connection.get_database_session()
    try:
        episode_db = session.query(EpisodeDB).filter(EpisodeDB.id == episode_id).first()
        if episode_db is None:
            raise AttributeError("Episode Not Found")

        episode_image = Image.open("./" + episode_db.image)
        session.close()
        if size != "original":
            episode_image.thumbnail(sizes[size])
        buffer = io.BytesIO()
        episode_image.save(buffer, format="webp")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/webp", status_code=200)
    except AttributeError:
        return StreamingResponse(
            io.BytesIO(b"Episode Not Found"), media_type="text/plain", status_code=404
        )


def get_episode_list_by_search(search: str = "", limit: int = 0, base_url: str = ""):
    """
    Search for episodes by name using a partial, case-insensitive match.

    Args:
        search (str): The search term to match against episode names.
        limit (int): The maximum number of episodes to return. If 0, no limit.
        base_url (str): The base URL for generating resource URLs.

    Returns:
        dict: A dictionary containing the list of matching episodes.

    """
    session = database_connection.get_database_session()
    try:
        query_episodes = (
            session.query(EpisodeDB)
            .filter(EpisodeDB.name.ilike(f"%{search}%"))
            .order_by(EpisodeDB.id.asc())
        )

        if limit != 0:
            query_episodes = query_episodes.limit(limit)
        episode_list = query_episodes.all()
        result = {"episodes": {}}
        for index, episode in enumerate(episode_list):
            result["episodes"][index] = Episode(episode, base_url).toJSON()

        if result == {"episodes": {}}:
            raise ValueError("Episode Not Found")
        return result
    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_episode_list(limit: int = 0, base_url: str = ""):
    """
    Get a list of all episodes, ordered by ID.

    Args:
        limit (int): The maximum number of episodes to return. If 0, no limit.
        base_url (str): The base URL for generating resource URLs.

    Returns:
        dict: A dictionary containing the list of episodes.

    """
    session = database_connection.get_database_session()
    try:
        query_episodes = session.query(EpisodeDB).order_by(EpisodeDB.id.asc())

        if limit != 0:
            query_episodes = query_episodes.limit(limit)
        episode_list = query_episodes.all()
        result = {"episodes": {}}
        for index, episode in enumerate(episode_list):
            result["episodes"][index] = Episode(episode, base_url).toJSON()
        return result
    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_episode_by_id(
    id: int, add_url: bool = False, base_url: str = "", metadata: bool = False
) -> dict:
    """
    Retrieve a specific episode from the database by its ID.

    Args:
        id (int): The unique identifier of the episode
        add_url (bool): Whether to include API URLs in the response
        base_url (str): The base URL for API endpoints
        metadata (bool): Whether to include metadata in the response

    Returns:
        dict: JSON response containing either:
            - Episode data if found
            - Error message if not found or database error occurred

    Response Format:
        Success:
            With add_url=True:
                {"name": str, "url": str}
            With add_url=False:
                {episode_data} or {"episode": episode_data, "metadata": {...}}

    Error:
            {"error": str, "status": "failed"}

    """
    session = database_connection.get_database_session()
    try:
        episode_db = session.query(EpisodeDB).filter(EpisodeDB.id == id).first()
        if episode_db is None:
            raise AttributeError("Episode Not Found")
        episode = Episode(episode_db, base_url)

        if add_url:
            return {
                "name": episode.model_dump()["name"],
                "url": f"{base_url}api/episodes/{id}",
            }

        total_episodes = session.query(EpisodeDB).count()
        session.close()
        return episode.toJSON(metadata, total_episodes)

    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_last_episode(base_url: str = "") -> dict:
    """
    Retrieve the most recent episode from the database.

    Returns:
        dict: JSON response containing either:
            - Latest episode data if found
            - Error message if database error occurred

    Response Format:
        Success:
            {episode_data}

    Error:
            {"error": str, "status": "failed"}

    """
    try:
        session = database_connection.get_database_session()
        episode_db = session.query(EpisodeDB).order_by(EpisodeDB.id.desc()).first()
        if episode_db is None:
            raise AttributeError("Episode Not Found")
        episode = Episode(episode_db, base_url)

        session.close()
        return episode.toJSON()

    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_episode(
    exclude_paramount_plus: bool = False, exclude_censored: bool = False, base_url=""
):
    """
    Get a random episode.

    Args:
        response (Response): FastAPI response object for status codes.
        request (Request): FastAPI request object containing base URL.
        exclude_paramount_plus (Boolean): If True excludes the Paramount+ episodes.
        exclude_censored (Boolean): If True excludes the censored episodes.
        base_url (str): The base URL for API endpoints

    Returns:
        dict: JSON response containing the episode data

    Response Format:
        Success:
            With add_url=False:
                {episode_data} or {"episode": episode_data, "metadata": {...}}

    Error:
            {"error": str, "status": "failed"}

    """
    session = database_connection.get_database_session()
    try:
        query = session.query(EpisodeDB)
        if exclude_paramount_plus:
            query.filter(EpisodeDB.paramount_plus_exclusive is False)
        if exclude_censored:
            query.filter(EpisodeDB.censored is False)
        episode_db = query.order_by(func.random()).first()
        if episode_db is None:
            raise AttributeError("Episode Not Found")
        episode = Episode(episode_db, base_url=base_url)
        return episode.toJSON()
    except AttributeError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
