"""
Module written by Carlos Chacón.

This module provides functionality to check the database connection status
and retrieve the PostgreSQL version information.
"""

from sqlalchemy import func
from sqlalchemy.exc import InvalidRequestError, OperationalError

from src.controller import database_connection


def get_database_status() -> dict:
    """
    Check database connectivity and get version information.

    Returns:
        dict: JSON response containing either:
            - Database version and connection status if successful
            - Error message if connection fails

    Response Format:
        Success:
            {
                "version": str,
                "status": "connected"
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    Example:
        Success:
            {
                "version": "PostgreSQL 15.4",
                "status": "connected"
            }

    """
    session = database_connection.get_database_session()
    try:
        # Use SQLAlchemy's func.version() to get the database version
        version_string = session.query(func.version()).scalar()
        return {"version": version_string, "status": "connected"}
    except OperationalError as e:
        return {"error": str(e), "status": "Database Not Available"}
    except InvalidRequestError as e:
        return {"error": str(e), "status": "The session in database was closed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        if session:
            session.close()
