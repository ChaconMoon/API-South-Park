"""
Module writted by Carlos Chacón.

Define the Album table model.
"""

from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base

if TYPE_CHECKING:
    from src.model.ORM.album_songs_db import AlbumSongDB  # noqa: F401


class AlbumDB(Base):
    """
    Contain a Album model from the Postgress database.

    Params:
    __tablename__ : The name of table in Postgress.

    id (SQLAlchemy Column [Integer PK]) : The ID of the album.
    name (SQLAlchemy Column [Text Not Null, Unique]) : The name of the album.
    release_date (SQLAlchemy Column [Date]) : The realese_date of the album.
    album_cover (SQLAlchemy Column [Text]) : The relative URL to the album cover image.
    album_url (SQLAlchemy Column [Text]) : the link of the album in Youtube Music or
    "NO AVAILABLE" text if it is no available
    web_album_cover (SQLAlchemy Column [Text]) : The URL to the cover image compresed.
    """

    __tablename__ = "albums"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    release_date = Column(Date)
    album_cover = Column(Text)
    album_url = Column(Text)
    web_album_cover = Column(Text)

    songs = relationship("AlbumSongDB", back_populates="album")
