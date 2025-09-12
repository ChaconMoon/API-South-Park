"""
Module written by Carlos Chacón.

This module get the param of the API in the get album operations, make the query to the API and return the result.
"""

# Import OS dependecies
import os
import time

# Import SQLAlquemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declarate Global variables to the connection and the sesion
_connection = None
_localSesion = None


def get_database_connection():
    """
    Start the connection with the database

    Returns:
        The connection with the database
    """

    # Get the global variables
    global _connection, _localSesion

    _connection = create_engine(
        os.getenv("DATABASE_URL"),  # Get the Databse URL from the env variables
        pool_size=5,  # Limit of the conecction with the database.
        max_overflow=10,  # Limit of the aditional conections
        pool_recycle=3600,  # Recycle conections per hour
        pool_pre_ping=True,  # Verify connection before use the databae
        pool_timeout=30,  # Limit time to get the conection with the databse
    )

    # Create the sesion in the database
    _localSesion = sessionmaker(autocommit=False, autoflush=False, bind=_connection)

    # Returns the connection with the databse
    return _connection


def get_database_session():
    """
    Get a session of the Database of there is a existing session only return it

    Returns:
        A session of the databse.
    """
    global _localSesion
    if _localSesion is None:
        get_database_connection()
    return _localSesion()


def get_query_result(statement: str, params: dict = {}):
    """
    Get a result of a query

    Params:
        statement (str): The basic statment of the query.
        params (dict): The params of the query.
    Returns:
        The query result
    """
    session = get_database_session()
    try:
        query_result = session.execute(statement, params)
        session.close()
        return query_result
    except Exception:
        time.sleep(1)
        try:
            query_result = session.execute(statement, params)
            session.close()
            return query_result
        except Exception:
            return None
    finally:
        session.close()
