"""
Module writted by Carlos Chacón.

Define the methods used to the miscellaneous endpoints.
"""
from fastapi.responses import JSONResponse

from src.controller.database_connection import get_database_session
from src.model.butters_punishments import ButtersPunishments
from src.model.ORM.butters_punishments_db import ButtersPunishmentsDB


def get_butters_punishment_by_id(id: int, base_url: str) -> dict:
    """
    Retrieve a Butters' punishment entry by its unique ID.

    Args:
        id (int): Unique identifier for the punishment
        base_url (str): Base URL of the API

    Returns:
        dict: JSON response containing the Butters'
          punishment data or an error message if not found

    """
    session = get_database_session()
    try:
        punishment_db = session.query(ButtersPunishmentsDB).filter_by(id=id).first()

        if not punishment_db:
            return {
                    "error": f"Butters' punishment with ID {id} not found.",
                    "status": "failed"
                }

        punishment = ButtersPunishments(db_object=punishment_db, base_url=base_url)
        return punishment.toJSON()
    except Exception as e:
            return {
                    "error": "An error occurred while retrieving the punishment.",
                    "details": str(e),
                    "status": "failed"
                }
    finally:
        session.close()
