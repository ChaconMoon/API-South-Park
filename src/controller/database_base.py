"""
Module writted by Carlos Chacón.

Define the Base class used in ORM models.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class used to create ORM Objects.

    Inherits from:
        DeclarativeBase: Base class used in SQLAlchemy ORM models.
    """

    pass
