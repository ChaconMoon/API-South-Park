"""
Module written by Carlos Chacón.

This Module defines the creator functions to create the web cards of the episodes
in the index website.
"""

import requests


def create_episode_web_card_to_website(base_url: str, episode_id: int) -> str:
    """
    Create a web card that contains an Episode in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            episode_id: The ID of the episode to create the card.

    Returns:
            ``str``: The string that defines the HTML code of the card.

    """
    request_url = f"{base_url}api/episodes/{episode_id}"
    request = requests.get(request_url, timeout=10)
    request_json = request.json()

    episode_name = request_json["name"]
    episode_image = request_json["episode_thumbnail"]
    episode_release_date = request_json["realese_date"]
    episode_description = request_json["description"]
    episode_status = request_json["episode_in_website"]["status"]
    # episode_url = request_json["episode_in_website"]["website_url"]

    return f"""
        <a href="{request_url}" target="blanck" class="episode_card_link">
                <div class="episode_card">
                        <img class="episode_image" src="{episode_image}" alt="Avatar">
                        <p class="episode_number">
                                <b>Episode: {episode_id}</b>
                        </p>
                        <p class="episode_name">
                                <b>Name: {episode_name}</b>
                        </p>
                        <div class="episode_description">
                                <p class="episode_description_text">
                                        <b>{episode_description}</b>
                                </p>
                                <p class="episode_status">STATUS: {episode_status}</p>
                                <p class="episode_release">{episode_release_date}</p>
                        </div>
                </div>
        </a>\n
        """


def create_episode_image_grid(ids: list[int], base_url: str) -> str:
    """
    Create a grid of the web cards that contain the Episodes in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of the IDs of the episodes to create the cards.

    Returns:
            ``str``: The string that defines the HTML code of the grid.

    """
    return "".join(create_episode_web_card_to_website(base_url, id) for id in ids)
