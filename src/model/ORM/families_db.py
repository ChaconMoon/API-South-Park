"""
Module writted by Carlos Chacón.

Define the Families table model.
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class FamilyDB(Base):
    """
    Contain a Family model of the Postgress database.

    Params:
    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the family.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the family.
    images (SQLAlchemy Column [ARRAY(TEXT)]) : A list of the images of the family.
    """

    __tablename__ = "families"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    images = Column(ARRAY(Text))
    characters = relationship("CharacterDB", back_populates="family")
