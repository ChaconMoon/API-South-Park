"""
Module writted by Carlos Chacón.

Define the songs in album table model and relationships.
"""

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base

if TYPE_CHECKING:
    from src.model.ORM.album_db import AlbumDB  # noqa: F401


class AlbumSongDB(Base):
    """
    Contain the model of the Songs in album of the Postgress Database.

    Params:
    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the song.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the song.
    album_id (SQLAlchemy Column [Integer FK Album ID]): The album from the song.
    lyrics (SQLAclchemy Column [Text]): The lyrics of the song.
    song_url (SQLAclchemy Column [Text]): The song link in Youtube Music.

    album SQLAlchemy Relationship [Album]): The relationship between album and song.
    """

    __tablename__ = "album_songs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    album_id = Column(Integer, ForeignKey("albums.id"))
    lyrics = Column(Text)
    song_url = Column(Text)

    # Use strings for relationship definitions
    album = relationship("AlbumDB", back_populates="songs")
