"""
Module writted by Carlos Chacón.

Define the ButtersPunishments table model.
"""
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base

if TYPE_CHECKING:
    from src.model.ORM.episode_db import EpisodeDB  # noqa: F401
class ButtersPunishmentsDB(Base):
    """
    Contain a ButtersPunishments model from the Postgress database.

    Params:
    __tablename__ : The name of table in Postgress.

    id (SQLAlchemy Column [Integer PK]) : The ID of the punishment.
    episode (SQLAlchemy Column [Integer Not Null]) :
      The episode number where the punishment happened.
    reason_of_punishment (SQLAlchemy Column [Text Not Null]) :
      The reason for the punishment.
    """

    __tablename__ = "butters_punishments"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    episode = Column(Integer, ForeignKey("episodes.id"), nullable=False)
    reason_of_punishment = Column(Text, nullable=False)

    episode_ref = relationship("EpisodeDB", back_populates="butters_punishments")
