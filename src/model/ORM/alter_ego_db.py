"""
Module writted by Carlos Chacón.

Define the AlerEgo table model and relationship.
"""

from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class AlterEgoDB(Base):
    """
    Contain the AlterEgo model from the Postgress Database.

    Params:
    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the alterego.
    original_character (SQLAlchemy Column [Integer PK FK Character.id]) :
    The ID of the character.

    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the alterego.
    images (SQLAlchemy Column [ARRAY(TEXT)]): URL to the Characters images.
    """

    __tablename__ = "alter_ego"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    original_character = Column(
        Integer, ForeignKey("characters.id"), nullable=False, primary_key=True
    )
    name = Column(Text)
    images = Column(ARRAY(Text))

    character = relationship("CharacterDB", back_populates="alteregos")
