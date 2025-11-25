"""
Module written by Carlos Chacón.

This module define the methods used to create the response of a Group item
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.group import Group


def get_group_by_id(id, base_url: str = ""):
    """
    Retrieve a Group by its identifier and return its JSON representation.

    Args:
        id:  (int) Identifier of the group to retrieve.
        base_url : (str) Base URL used to construct item links in the Group representation

    Returns:
        dict JSON-serializable representation of the Group.

    """
    query_result = get_query_result(
        text(
            """
            SELECT c.*
            FROM public.characters_group cg join public.characters c
            ON cg.id_character = c.id
            where cg.id_group = :id
            ORDER BY id_character ASC
            """
        ),
        {"id": id},
    )
    group = Group(id, query_result, base_url)
    return group.toJSON()
