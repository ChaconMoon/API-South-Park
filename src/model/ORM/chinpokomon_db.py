"""
Module writted by Carlos Chacón.

Define the chinpokomon table model.
"""

from sqlalchemy import Column, Integer, Text

from src.controller.database_base import Base


class ChinpokomonDB(Base):
    """
    Contain a Chinpokomon object from the database.

    Params:
    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the chinpokomon.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the chinpokomon.
    image (SQLAlchemy Column [Text Not Null, Unique]): The image of the chinpokomon.
    """

    __tablename__ = "chinpokomon"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    image = Column(Text, nullable=False, unique=True)
