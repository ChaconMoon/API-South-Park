"""
Module written by Carlos Chacón.

This Module defines the creator functions to create the web cards of alter egos
in the index website.
"""

import requests

from src.website_elements.create_character_card_web import (
    create_character_web_card_to_website,
)


def create_alter_ego_web_card_to_website(
    base_url: str, character_id: int, alter_egos_ids: list[int]
) -> str:
    """
    Create a web card that contains a Character and their Alter Egos in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            character_id: The ID of the main character.
            alter_egos_ids: List of IDs for the character's alter egos.

    Returns:
            ``str``: The string that defines the HTML code of the card.

    """
    alter_ego_containers = "".join(
        f"""<div class="alter_ego_container">
        <a href="{base_url}api/characters/{character_id}/alteregos/{
            id + 1
        }" target="blanck" class="alter_ego_link">
        <img src="{
            requests.get(
                f"{base_url}api/characters/{character_id}/alteregos/{id + 1}", timeout=10
            ).json()["images"][0]
        }"/>
        <p class="alter_ego_name">
        {
            requests.get(
                f"{base_url}api/characters/{character_id}/alteregos/{id + 1}", timeout=10
            ).json()["name"]
        }
        </p>
        </a>
        </div>\n"""
        for id in alter_egos_ids
    )

    return f"""
                <div class="character_and_alterego_grid">
                {create_character_web_card_to_website(base_url, character_id)}
                <div class="alter_egos_container">
                {alter_ego_containers}
                </div>
                </div>
                """


def create_alter_ego_image_grid(ids: list[list[int]], base_url: str) -> str:
    """
    Create a grid of web cards that contain Characters and their Alter Egos.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of lists containing character IDs and their alter ego IDs.

    Returns:
            ``str``: The string that defines the HTML code of the grid.

    """
    return "".join(
        create_alter_ego_web_card_to_website(base_url, character[0], character[1:])
        for character in ids
    )
