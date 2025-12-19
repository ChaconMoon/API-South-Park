"""
Module writted by Carlos Chacón.

Define the group table model and relationship.
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base
from src.controller.database_connection import get_character_group_table


class GroupDB(Base):
    """
    Contain the model of the Groups Table in Postgress.

    Params:
    id (SQLAlchemy Column [Integer PK]) :  The ID of the group.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the group.
    images (SQLAlchemy Column [TEXT]) : A list of the images of the group.
    """

    __tablename__ = "groups"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    image = Column(Text)

    characters = relationship(
        "CharacterDB", secondary=get_character_group_table(), back_populates="groups"
    )
