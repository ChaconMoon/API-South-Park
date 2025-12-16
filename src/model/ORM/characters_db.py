"""
Module writted by Carlos Chacón.

Define the Character table model and relationships.
"""

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from src.controller.database_base import Base
from src.controller.database_connection import get_character_group_table

if TYPE_CHECKING:
    from src.model.ORM.alter_ego_db import AlterEgoDB  # noqa: F401
    from src.model.ORM.episode_db import EpisodeDB  # noqa: F401
    from src.model.ORM.families_db import FamilyDB  # noqa: F401
    from src.model.ORM.groups_db import GroupDB  # noqa: F401


class CharacterDB(Base):
    """
    Contain a Character model of the Postgress database.

    Params:
    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the character.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the character.
    family (SQLAlchemy Column [Integer FK Family ID]): The id of the character's family.
    birthday (SQLAlchemy Column [TEXT]) : The bithday of the character. Example: 'January 1st'
    religion (SQLAlchemy Column [ARRAY(TEXT)]) : A list of the religions of the character.
    firt_apperance (SQLAlchemy Column [Integer FK Episode ID, Not Null]) : the episode where the character debuts.
    images (SQLAlchemy Column [ARRAY(TEXT)]) : A list of the images of the character.
    famous_guest (SQLAlchemy Column [Boolean]): If the character is a famous guest.
    family (SQLAlchemy Relationship [Family]): The relationship between character and family.
    debut (SQLAlchemy Relationship [Episode]): The relationship between character and episode.
    """  # noqa: E501

    __tablename__ = "characters"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    family_id = Column(Integer, ForeignKey("families.id"))
    birthday = Column(Text)
    age = Column(Integer)
    religion = Column(ARRAY(Text))
    debut_episode = Column(Integer, ForeignKey("episodes.id"), nullable=False)
    images = Column(ARRAY(Text))
    famous_guest = Column(Boolean)
    family = relationship("FamilyDB", back_populates="characters")
    debut = relationship("EpisodeDB", back_populates="debut_characters")
    alteregos = relationship("AlterEgoDB", back_populates="character")
    groups = relationship(
        "GroupDB", secondary=get_character_group_table(), back_populates="characters"
    )
