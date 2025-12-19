"""
Module writted by Carlos Chacón.

Define the games table model.
"""

from sqlalchemy import Column, Date, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY

from src.controller.database_base import Base


class GameDB(Base):
    """
    Contain a game object from the Postgress database.

    Params:

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the game.
    name (SQLAlchemy Column [Text Not Null, Unique]) : The name of the game.
    developer (SQLAlchemy Column [Text]) : The developer of the game.
    platforms (SQLAlchemy Column [ARRAY(TEXT)]):
    A list with the platforms where the game is available.

    release_date (SQLAlchemy Column [Date]) : The realese_date of the gmae.
    images (SQLAlchemy Column [ARRAY(TEXT)]) : A list with images of the game.
    """

    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True, unique=True)
    developer = Column(Text)
    platforms = Column(ARRAY(Text))
    release_date = Column(Date)
    images = Column(ARRAY(Text))
