"""
Module writted by Carlos Chacón.

Define the FortniteCosmeticsRarity table model.
"""


from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from src.controller.database_base import Base


class FortniteCosmeticDB(Base):
    """
    Contain a instance of the FortniteCosmetic in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the cosmetic.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the cosmetic.
    type_id (SQLAlchemy Column [Integer FK Not Null]) :
      The foreign key to the FortniteCosmeticTypes table.
    rarity_id (SQLAlchemy Column [Integer FK Not Null]) :
      The foreign key to the FortniteCosmeticsRarity table.
    image (SQLAlchemy Column [Text Not Null]) : The thumbnail of the cosmetic.
    price (SQLAlchemy Column [Integer]) : The price of the cosmetic in V-Bucks.
    notes (SQLAlchemy Column [Text]) : Additional notes about the cosmetic.

    type_ref (SQLAlchemy Relationship [FortniteCosmeticTypesDB]):
    The relationship between cosmetic and its type.

    rarity_ref (SQLAlchemy Relationship [FortniteCosmeticsRarityDB]):
    The relationship between cosmetic and its rarity.

    """

    __tablename__ = "fortnite_cosmetics"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    type = Column(
        Integer,
        ForeignKey("fortnite_cosmetic_types.id"),
        nullable=False
    )
    rarity = Column(
        Integer,
        ForeignKey("fortnite_cosmetic_rarities.id"),
        nullable=False
    )
    price = Column(Integer, nullable=True)
    images = Column(ARRAY(Text))
    notes = Column(Text, nullable=True)

    type_ref = relationship("FortniteCosmeticTypesDB", back_populates="cosmetics_with_type")
    rarity_ref = relationship("FortniteCosmeticsRarityDB", back_populates="cosmetics_with_rarity")