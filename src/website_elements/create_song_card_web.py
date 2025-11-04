"""
Module written by Carlos Chacón.

This Module define the crators of functions to create the
 web cards of the songs in the index.
"""

import requests


def create_song_web_card_to_website(base_url: str, song_id: int) -> str:
    """
    Create a web card that contain a Songs in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            song_id: The ID of the song to create the card.

    Retruns:
            ``str``: The string that defines the HTML code of the card.
    """
    song_request_url = f"{base_url}api/songs/{song_id}"
    request = requests.get(song_request_url, timeout=10)

    request_json = request.json()

    song_name = request_json["name"]
    album_number = int(request_json["album_number"])
    song_url = request_json["song_url"]

    request_url = f"{base_url}api/albums/{album_number}"
    request = requests.get(request_url, timeout=10)
    request_album_json = request.json()

    album_name = request_album_json["name"]
    album_release = request_album_json["release_date"]

    album_cover = request_album_json["web_album_cover"]

    html_button = (
        """
        <div class="not_avalible_button">
        Not Avalible
        </div>
        """
        if song_url == "[NOT AVAILABLE IN STREAMING SERVICES]"
        else f"""
        <a href="{song_url}" class="play_button">
        <div>
        Play ▶
        </div>
        </a>
    """
    )
    html_response = f"""
        <div class="song_card" >
                <a href="{song_request_url}" target="blanck" class="song_card_link">
                                <img class="album_image" src="{album_cover}" alt="Cover">
                                <p class="song_name">
                                        <b>{song_name}</b>
                                </p>
                                <p class="album_name_in_song_menu">
                                        Album: {album_name}
                                </p>
                                        <p class="album_release">
                                        Release Date: {album_release}
                                </p>
                </a>\n
                {html_button}
        </div>
        """
    return html_response


def create_song_image_grid(ids: list[int], base_url: str) -> str:
    """
    Create a grid of the web card that contain the Songs in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of the IDs of the songs to create the card.

    Retruns:
           ``str``: The string that defines the HTML code of the card.
    """
    divs_containers = ""
    for id in ids:
        divs_containers += create_song_web_card_to_website(base_url, id)
    return divs_containers
