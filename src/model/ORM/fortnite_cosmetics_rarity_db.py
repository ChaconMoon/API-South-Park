"""
Module writted by Carlos Chacón.

Define the FortniteCosmeticsRarity table model.
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class FortniteCosmeticsRarityDB(Base):
    """
    Contain a instance of the FortniteCosmeticsRarity in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the rarity.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the rarity.


    cosmetics (SQLAlchemy Relationship [FortniteCosmeticDB]):
    The relationship between cosmetics and their rarity.

    """

    __tablename__ = "fortnite_cosmetic_rarities"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    cosmetics_with_rarity = relationship(
        "FortniteCosmeticDB",
        back_populates="rarity_ref",
    )
