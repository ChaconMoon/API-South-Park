"""
Module written by Carlos Chacón.

This module handles date-related operations for the South Park API.
It provides functions to check birthdays and retrieve characters that have
their birthday on the current date.
"""

import logging
from datetime import datetime

from src.controller import database_connection
from src.model.ORM.characters_db import CharacterDB


def get_today_birthday() -> str:
    """
    Get today's date formatted as 'Month Day' with proper ordinal suffix.

    Returns:
        str: Formatted date string (e.g., 'November 3rd')

    Example:
        If today is November 3rd:
            get_today_birthday() -> 'November 3rd'

    """
    actual_date = datetime.now()
    month = actual_date.strftime("%B")
    day = actual_date.strftime("%d")

    match day:
        case day if day in ["1", "21", "31"]:
            day += "st"
        case day if day in ["2", "22"]:
            day += "nd"
        case day if day in ["3", "23"]:
            day += "rd"
        case _:
            day += "th"

    return f"{month} {day}"


def get_today_birthday_character(base_url: str = "") -> dict:
    """
    Get all characters that have their birthday on the current date.

    Args:
        base_url (str): Base URL for API endpoints and assets

    Returns:
        dict: JSON response containing either:
            - List of characters with today's birthday
            - Message if no birthdays today
            - Error message if database error

    Response Format:
        Success:
            {
                "characters": [
                    {character_data},
                    {character_data},
                    ...
                ]
            }
        No Birthdays:
            {
                "message": "No one has their birthday today",
                "status": "failed"
            }

    Error:
            {
                "error": str,
                "status": "failed"
            }

    """
    try:
        birthay_characters_list = (
            database_connection.get_database_session()
            .query(CharacterDB)
            .filter(CharacterDB.birthday == get_today_birthday())
            .all()
        )

        if not birthay_characters_list:
            return {"message": "No one has their birthday today", "status": "failed"}

        result = {"characters": []}
        for birthday_character in birthay_characters_list:
            result["characters"].append(
                {
                    "name": birthday_character.name,
                    "url": f"{base_url}api/characters/{birthday_character.id}",
                }
            )

        return result

    except Exception as e:
        logging.error(e)
        return {"error": str(e), "status": "failed"}
