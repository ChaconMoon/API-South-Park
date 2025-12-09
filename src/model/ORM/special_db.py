"""
Module writted by Carlos Chacón.

Define the Special table model.
"""

from sqlalchemy import Column, Date, Integer, Text

from src.controller.database_base import Base


class SpecialDB(Base):
    """
    Contain a instance of the Episode in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the character.
    title (SQLAlchemy Column [Text Not Null, Unique]): The title of the special.
    release_date (SQLAlchemy Column [Date]) : The realese_date of the special.
    description (SQLAlchemy Column [Text]) : Description of the episode.
    link (SQLAlchemy Column [Text]) : The URL on Paramount Plus.
    poster (SQLAlchemy Column [Text]) : The poster of the special.
    """

    __tablename__ = "specials"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True)
    release_date = Column(Date)
    link = Column(Text)
    description = Column(Text)
    poster = Column(Text)
