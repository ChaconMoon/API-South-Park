"""
Module written by Carlos Chacón.

This module define the methods used to create the response of a Group item
"""

from sqlalchemy import text

from src.controller.database_connection import get_query_result
from src.model.group import Group, get_group_name_by_id


def get_group_by_id(id, base_url: str = "", metadata=False):
    """
    Retrieve a Group by its identifier and return its JSON representation.

    Args:
        id:  (int) Identifier of the group to retrieve.
        base_url : (str) Base URL used to construct item links in the Group representation
        metadata : (bool) If the result must return metadata

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
    if query_result is None:
        return {"error": "Database not available", "status": "failed"}
    elif query_result.rowcount == 0 and get_group_name_by_id(id) is None:
        return {"error": "Group not found", "status": "failed"}

    group = Group(id, query_result, base_url)

    query_result = get_query_result(text("""SELECT * FROM public.groups"""))

    return group.toJSON(metadata, total_results=query_result.rowcount)


def get_random_group(base_url: str = ""):
    """
    Retrieve a random Group and return its JSON representation.

    Args:
        base_url : (str) Base URL used to construct item links in the Group representation

    Returns:
        dict JSON-serializable representation of the Group.

    """
    # 1. Get a random group ID from groups that have members
    id_query_result = get_query_result(
        text(
            """
            SELECT "ID" FROM public.groups
            ORDER BY RANDOM()
            LIMIT 1
            """
        )
    )

    if id_query_result is None:
        return {"error": "Database not available", "status": "failed"}
    if id_query_result.rowcount == 0:
        return {"error": "No groups with characters found", "status": "failed"}

    id = id_query_result.scalar_one()

    # 2. Get all characters for that specific group ID
    characters_query_result = get_query_result(
        text(
            """
            SELECT c.*
            FROM public.characters_group cg JOIN public.characters c
            ON cg.id_character = c.id
            WHERE cg.id_group = :id
            ORDER BY id_character ASC
            """
        ),
        {"id": id},
    )

    if characters_query_result is None:
        return {"error": "Database not available", "status": "failed"}

    # 3. Create the Group object with the full result set
    group = Group(id, characters_query_result, base_url)

    return group.toJSON()
