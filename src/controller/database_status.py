"""
Module written by Carlos Chacón.

This module provides functionality to check the database connection status
and retrieve the PostgreSQL version information.
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result


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
