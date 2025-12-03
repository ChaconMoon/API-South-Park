"""
Module writted by Carlos Chacón.

Define the Episode table model.
"""

from sqlalchemy import Boolean, Column, Date, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class EpisodeDB(Base):
    """Docstring for EpisodeDB."""

    __tablename__ = "episodes"

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
    characters = relationship("CharacterDB", back_populates="debut")
