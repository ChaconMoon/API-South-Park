"""
Module written by Carlos Chacón.

This module make a query to verify if the Databse is avalible.
"""

# Import SQLAlchemy
from sqlalchemy import text

# Internal Imports
from src.controller.database_connection import get_query_result


# Get the status of the database
def get_database_status():
    """
    Retruns:
        A dict with the version and the status of the databse.
    """
    rows = dict()
    try:
        query_result = get_query_result(text("SELECT version()"))
        for row in query_result:
            rows["version"] = str(row[0])
            rows["status"] = "connected"
    except Exception as e:
        rows["error"] = str(e)
        rows["status"] = "failed"
    return rows
