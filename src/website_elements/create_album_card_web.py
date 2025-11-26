"""
Module written by Carlos Chacón.

This Module defines the creator functions to create the web cards of albums
in the index website.
"""

import requests


def create_album_web_card_to_website(base_url: str, album_id: int) -> str:
    """
    Create a web card that contains an Album in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            album_id: The ID of the album to create the card.

    Returns:
            ``str``: The string that defines the HTML code of the card.

    """
    request_url = f"{base_url}api/albums/{album_id}"
    request = requests.get(request_url, timeout=10)
    request_album_json = request.json()

    album_name = request_album_json["name"]
    album_release = request_album_json["release_date"]
    album_cover = request_album_json["web_album_cover"]
    album_url = request_album_json["album_url"]

    html_button = (
        """
        <div class="album_not_available_button">
        Not Available
        </div>
        """
        if album_url == "NOT AVAILABLE"
        else f"""
        <a href="{album_url}" target="blanck" class="album_play_button">
        <div>
        Play ▶
        </div>
        </a>
        """
    )

    return f"""
        <div class="album_card">
                <a href="{request_url}" target="blanck" class="album_card_link">
                        <img class="album_image" src="{album_cover}" alt="Cover">
                        <p class="album_name">
                                <b>{album_name}</b>
                        </p>
                        <p class="album_release">
                                Release Date: {album_release}
                        </p>
                </a>
                {html_button}
        </div>
        """


def create_album_image_grid(ids: list[int], base_url: str) -> str:
    """
    Create a grid of web cards that contain the Albums in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of the IDs of the albums to create the cards.

    Returns:
            ``str``: The string that defines the HTML code of the grid.

    """
    return "".join(create_album_web_card_to_website(base_url, id) for id in ids)
