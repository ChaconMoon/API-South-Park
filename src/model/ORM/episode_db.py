"""
Module writted by Carlos Chacón.

Define the Episode table model.
"""

from sqlalchemy import Boolean, Column, Date, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class EpisodeDB(Base):
    """
    Contain a instance of the Episode in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the character.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the character.
    season (SQLAlchemy Column [Integer Not Null]) : The season of the Episode.
    episode (SQLAlchemy Column [Integer Not Null]) : The episode in the season.
    release_date (SQLAlchemy Column [Date]) : The realese_date of the episode.
    description (SQLAlchemy Column [Text]) : Description of the episode.
    website_url (SQLAlchemy Column [Text]) : The URL in South Park Website.
    censored (SQLAlchemy Column [Boolean]) : If the episode is censored.
    paramount_plus_exclusive (SQLAlchemy Column [Boolean]) :
    If the episode is exclusive of Paramount Plus.

    image (SQLAlchemy Column [Text]) : The thumbnail of the episode.
    debut_characters (SQLAlchemy Relationship [Episode]):
    The relationship between character and episode.

    """

    __tablename__ = "episodes"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    season = Column(Integer, nullable=False)
    episode = Column(Integer, nullable=False)
    release_date = Column(Date)
    description = Column(Text)
    website_url = Column(Text)
    censored = Column(Boolean)
    paramount_plus_exclusive = Column(Boolean)
    image = Column(Text)
    debut_characters = relationship("CharacterDB", back_populates="debut")
