"""
Module written by Carlos Chacón.

This module handles database connectivity for the South Park API. It manages
database connections, sessions, and query execution using SQLAlchemy. The module
implements connection pooling and retry logic for improved reliability.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import sessionmaker

from src.controller.database_base import Base

# Global connection variables
_connection = None
_localSesion = None
character_group = None


def get_database_connection():
    """
    Initialize and return a database connection with pooling configuration.

    Creates a new connection if none exists, using environment variables for
    connection parameters.

    Returns:
        SQLAlchemy Engine: Configured database connection engine

    Connection Parameters:
        pool_size: Maximum number of permanent connections
        max_overflow: Maximum number of additional temporary connections
        pool_recycle: Time (seconds) before connections are recycled
        pool_pre_ping: Whether to verify connection before use
        pool_timeout: Maximum time to wait for connection

    """
    global _connection, _localSesion, character_group
    load_dotenv()

    if _connection:
        return _connection

    _connection = create_engine(
        os.getenv("SOUTHPARK_DATABASE_URL"),
        pool_size=5,
        max_overflow=10,
        pool_recycle=3600,
        pool_pre_ping=True,
        pool_timeout=30,
    )
    character_group = Table(
        "characters_group",
        Base.metadata,
        autoload_with=_connection,  # lee la estructura existente de PostgreSQL
    )

    _localSesion = sessionmaker(autocommit=False, autoflush=False, bind=_connection)
    return _connection


def get_character_group_table():
    """
    Devuelve el objeto Table de SQLAlchemy para 'character_group'.

    Inicializa la conexión a la base de datos si es necesario.

    Returns:
        SQLAlchemy Table: Objeto que representa la tabla 'character_group'.

    """
    if character_group is None:
        get_database_connection()
    return character_group


def get_database_session():
    """
    Get or create a database session.

    Returns an existing session if available, otherwise creates a new one.

    Returns:
        SQLAlchemy Session: Database session object for executing queries

    """
    global _localSesion
    if _localSesion is None:
        get_database_connection()
    return _localSesion()
