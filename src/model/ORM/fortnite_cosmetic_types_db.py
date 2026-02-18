"""
Module writted by Carlos Chacón.

Define the FortniteCosmeticTypes table model.
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class FortniteCosmeticTypesDB(Base):
    """
    Contain a instance of the FortniteCosmeticTypes in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the cosmetic type.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the cosmetic type.


    cosmetics (SQLAlchemy Relationship [FortniteCosmeticDB]):
    The relationship between cosmetics and their type.

    """

    __tablename__ = "fortnite_cosmetic_types"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    type = Column(Text, nullable=False, unique=True)
    cosmetics_with_type = relationship(
        "FortniteCosmeticDB",
        back_populates="type_ref"
    )
