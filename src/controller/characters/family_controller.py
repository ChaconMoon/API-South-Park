"""
Module written by Carlos Chacón.

This module get the param of the API in the get family operations,
make the query to the API and return the result.
"""

# Import SQLAlchemy
import io

from fastapi import Response
from fastapi.responses import StreamingResponse
from PIL import Image
from sqlalchemy import func
from sqlalchemy.exc import DataError, OperationalError

from src.controller import database_connection
from src.model.family import Family

# Interal Inputs
from src.model.ORM.families_db import FamilyDB


def get_family_image(family_id: int, image_id : int, size: str) -> StreamingResponse:
    """
    Get the image of a family.

    :param family_id: The id of the family.
    :type family_id: int
    :param image_id: The id of the image [Starts in 1].
    :type image_id: int
    :param size: The size of the image.
    :type size: str
    :return: The image of the family.
    :rtype: StreamingResponse.
    """
    sizes = {
        "large": (1280,720),
        "medium": (960,540),
        "small": (640, 480)
    }
    try:
        session = database_connection.get_database_session()

        family_db = session.query(FamilyDB).filter(FamilyDB.id == family_id).first()
        if family_db is None:
            return Response(status_code=404)
        try:
            image = Image.open("./"+family_db.images[image_id-1])
        except IndexError:
            return Response(status_code=404)
        if size != "original":
            image.thumbnail(sizes[size])
        buffer = io.BytesIO()
        image.save(buffer,format="PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png", status_code=200)
    finally:
        session.close()

def get_family_list(limit: int = 0, base_url="") -> dict:
    """
    Return a list of families.

    :param limit: The number of families returned
    :type limit: int

    :param base_url: The URL used to create the absolute URL in response.
    :type base_url: str

    :return: A dict with the families.
    :rtype: dict
    """
    session = database_connection.get_database_session()
    try:
        if limit != 0:
            family_list = session.query(FamilyDB).limit(limit).all()
        else:
            family_list = session.query(FamilyDB).all()

        if family_list == []:
            raise DataError("No Families Found")
        result = dict()
        result["families"] = []
        result["families"].extend(
            Family(family_db, base_url=base_url) for family_db in family_list
        )
        return result

    except DataError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_family_search(search: str, limit: int = 0, base_url="") -> dict:
    """
    Retiurn the result of a family search.

    :param search: The param used in the search.
    :type search: str

    :param limit: The number of families returned.
    :type limit: int

    :param base_url: The URL used to create the absolute URL.
    :type base_url: str
    :return: A dict with the families
    :rtype: dict

    """
    session = database_connection.get_database_session()
    family_query = session.query(FamilyDB).filter(FamilyDB.name.ilike((f"%{search}%")))
    try:
        if limit != 0:
            family_query.limit(limit)
        family_list = family_query.all()
        if family_list == []:
            raise ValueError("Not families found")
        result = dict()
        result["families"] = []
        result["families"].extend(
            Family(family_db, base_url=base_url) for family_db in family_list
        )

        return result
    except ValueError as e:
        return {"error": str(e), "status": "Not Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


# Connection with the database
def get_family_by_id(id: int, url="", metadata=False) -> dict:
    """
    Get the ID of one familiy at return the data of this family and all they members.

    Params:
        id (int): The id of the family.
        url (str): The URL used.
    Retruns:
        A dict with the data of the family.
    """
    session = database_connection.get_database_session()
    try:
        family_db = session.query(FamilyDB).filter(FamilyDB.id == id).first()
        if family_db is None:
            raise ValueError("Family not found")
        family = Family(family_db, base_url=url)

        # Get the result of the query to the databse.
        total_families = session.query(func.count(FamilyDB.id)).scalar()

        return family.toJSON(metadata, total_results=total_families)

    # Control exceptions
    except ValueError as e:
        return {"error": str(e), "status": "Not Family Found"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        session.close()


def get_random_family(base_url="") -> dict:
    """
    Get one random familiy at return the data of this family and all they members.

    Params:
        base_url (str): The URL used.
    Retruns:
        A dict with the data of the family.
    """
    # Create variable to store the result data.
    session = database_connection.get_database_session()
    try:
        # Get the result of the query to the databse.
        family = Family(
            session.query(FamilyDB).order_by(func.random()).first(), base_url=base_url
        )

        return family.toJSON()

    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    # Control exceptions
    except Exception as e:
        return {"error": str(e), "status": "failed"}
