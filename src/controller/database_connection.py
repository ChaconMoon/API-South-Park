import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_connection = None
_localSesion = None


def get_database_connection():
    global _connection, _localSesion
    _connection = create_engine(
        os.getenv("DATABASE_URL"),
        pool_size=5,  # Conexiones permanentes en el pool
        max_overflow=10,  # Conexiones adicionales permitidas
        pool_recycle=3600,  # Reciclar conexiones cada hora
        pool_pre_ping=True,  # Verificar conexión antes de usar
        pool_timeout=30,  # Timeout para obtener conexión del pool                    # Cambiar a True para debug SQL
    )
    _localSesion = sessionmaker(autocommit=False, autoflush=False, bind=_connection)
    return _connection


def get_database_session():
    global _localSesion
    if _localSesion is None:
        get_database_connection()
    return _localSesion()


def get_query_result(statement: str, params: dict = {}):
    session = get_database_session()
    try:
        query_result = session.execute(statement, params)
        session.close()
        return query_result
    except Exception:
        return None
    finally:
        session.close
