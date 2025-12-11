"""
Module written by Carlos Chacón.

This module get the param of the API in the get alter ego operations,
make the query to the API and return the result.
"""

from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from src.controller import database_connection
from src.model.alter_ego import AlterEgo
from src.model.ORM.alter_ego_db import AlterEgoDB


# Get one Alter Ego by the character and id
def get_alter_ego_by_character_and_id(
    id_alter_ego: int, id_character: int, add_url=False, base_url="", metadata=False
):
    """
    Get one alter ego of the database.

    Args:
        id_alter_ego (int): The id of a ater_ego of the character.
        id_character (int): The id of the character of the alter ego.
        add_url (bool): If the response must contain the URL of the API.
        base_url (str): "The URL base of the API.
        metadata (bool): If the response must cotain metadata.

    Returns:
        The JSON Response

    """
    session = database_connection.get_database_session()
    try:
        alterego_db = (
            session.query(AlterEgoDB)
            .filter(
                AlterEgoDB.id == id_alter_ego,
                AlterEgoDB.original_character == id_character,
            )
            .first()
        )
        if alterego_db is None:
            raise ValueError("AlterEgo Not Found")
        alter_ego = AlterEgo(alterego_db, base_url)

        # Return the result with the URL
        if add_url:
            result = dict()
            result["name"] = alter_ego.model_dump()["name"]
            result["url"] = (
                f"{base_url}api/characters/{id_character}/alteregos/{id_alter_ego}"
            )
            return result

        alter_ego_count = (
            session.query(AlterEgoDB)
            .filter(AlterEgoDB.original_character == id_character)
            .count()
        )

        return alter_ego.toJSON(metadata, alter_ego_count)
    # Control exceptions
    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


# Get all the alter egos of a character
def get_all_alteregos_of_a_character(id_character: int, add_url=False, base_url=""):
    """
    Get one alter ego of the database.

    Args:
        id_character (int): The id of the character of the alter ego.
        add_url (bool): If the response must contain the URL of the API.
        base_url (str): "The URL base of the API.

    Returns:
        The JSON Response

    """
    session = database_connection.get_database_session()
    try:
        alterego_list_db = (
            session.query(AlterEgoDB)
            .filter(AlterEgoDB.original_character == id_character)
            .all()
        )

        result = {"alteregos": []}
        if alterego_list_db == []:
            raise ValueError("AlterEgos Not Found")
        result["alteregos"].extend(
            AlterEgo(alterego_db, base_url) for alterego_db in alterego_list_db
        )
        return result
    # Control exceptions
    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_alterego(character: int = 0, base_url=""):
    """
    Get one random alter ego of the database.

    Args:
        character (int): If is not 0, limit the response to One Character
        base_url (str): "The URL base of the API.

    Returns:
        The JSON Response

    """
    session = database_connection.get_database_session()
    try:
        if character != 0:
            alterego_db = (
                session.query(AlterEgoDB)
                .filter(AlterEgoDB.original_character == character)
                .order_by(func.random())
                .first()
            )
        else:
            alterego_db = session.query(AlterEgoDB).order_by(func.random()).first()
        alterego = AlterEgo(alterego_db, base_url)
        return alterego.toJSON()
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()
