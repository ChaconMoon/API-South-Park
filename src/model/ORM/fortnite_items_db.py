"""
Module writted by Carlos Chacón.

Define the FortniteItems table model.
"""

from sqlalchemy import Column, Integer, Text

from src.controller.database_base import Base


class FortniteItemsDB(Base):
    """
    Contain a instance of the FortniteItems in the database.

    __tablename__ : The name of the table in Postgress.
    id (SQLAlchemy Column [Integer PK]) :  The ID of the item.
    name (SQLAlchemy Column [Text Not Null, Unique]): The name of the item.
    image (SQLAlchemy Column [Text Not Null]) : The thumbnail of the item.
    effect (SQLAlchemy Column [Text]) : The effect of the item.

    type_ref (SQLAlchemy Relationship [FortniteItemTypesDB]):
    The relationship between item and its type.

    rarity_ref (SQLAlchemy Relationship [FortniteItemsRarityDB]):
    The relationship between item and its rarity.

    """

    __tablename__ = "fortnite_items"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    image = Column(Text, nullable=False)
    effect = Column(Text, nullable=True)