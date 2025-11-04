"""
Module written by Carlos Chacón.

This Module defines the creator functions to create the web cards of the games
in the index.
"""

import requests

PLATFORM_ICONS = {
    "XSeries": "https://img.icons8.com/?size=100&id=LqoHSNcZYyaZ&format=png&color=000000",
    "Dreamcast": "https://img.icons8.com/?size=100&id=60853&format=png&color=000000",
    "Web": "https://img.icons8.com/?size=100&id=119124&format=png&color=000000",
    "XOne": "https://img.icons8.com/?size=100&id=sHyMKmljmlSj&format=png&color=000000",
    "PC": "https://img.icons8.com/?size=100&id=12908&format=png&color=000000",
    "X360": "https://icons.iconarchive.com/icons/sykonist/console/128/Xbox-360-icon.png",
    "PS4": "https://img.icons8.com/?size=100&id=08OaSZHbTdVv&format=png&color=000000",
    "Escape Room": "https://img.icons8.com/?size=100&id=12824&format=png&color=000000",
    "PS5": "https://img.icons8.com/?size=100&id=J2arZBwbzFfE&format=png&color=000000",
    "Switch": "https://img.icons8.com/?size=100&id=E3bXXtS09hA1&format=png&color=000000",
    "IOS": "https://img.icons8.com/?size=100&id=20821&format=png&color=000000",
    "PS1": "https://images.icon-icons.com/829/PNG/128/Playsystem_icon-icons.com_66601.png",
    "Blackberry OS": "https://img.icons8.com/?size=100&id=xShzmmrWad9Y&format=png&color=000000",
    "N64": "https://img.icons8.com/?size=100&id=40979&format=png&color=000000",
    "PS3": "https://img.icons8.com/?size=100&id=68102&format=png&color=000000",
    "PSVita": "https://img.icons8.com/?size=100&id=TLejNLu7fP0N&format=png&color=000000",
    "GBC": "https://img.icons8.com/?size=100&id=p4IZ3gBGGvWo&format=png&color=000000",
    "Pinball Machine": "https://cdn-icons-png.flaticon.com/512/7960/7960368.png",
}

DEFAULT_ICON = "https://img.icons8.com/?size=100&id=DoFiicbRPzDS&format=png&color=000000"


def get_platform_icon_div(platform: str) -> str:
    """Create HTML div for a platform icon."""
    icon_url = PLATFORM_ICONS.get(str(platform), DEFAULT_ICON)
    return f'''<div class="platform_icon">
            <img src="{icon_url}">
            </div>
             '''


def create_platforms_grid(platforms: list) -> str:
    """Create HTML grid of platform icons."""
    return "".join(get_platform_icon_div(platform) for platform in platforms)


def create_game_card_html(game_data: dict, request_url: str) -> str:
    """Create HTML for a game card."""
    return f"""
        <a href="{request_url}" target="blanck" class="game_card_link">
                <div class="game_card">
                        <img class="game_image"
                         src="{game_data["images"][0]}" alt="Cover">
                        <p class="game_name">
                                <b>{game_data["name"]}</b>
                        </p>
                        <p class="game_release_date">
                                Release Date: {game_data["release_date"]}
                        </p>
                        <div class="platforms_grid">
                                {create_platforms_grid(game_data["platforms"])}
                        </div>
                </div>
        </a>\n
        """


def create_game_web_card_to_website(base_url: str, game_id: int) -> str:
    """Create a web card that contains a Game in the Index Website."""
    request_url = f"{base_url}api/games/{game_id}"
    request = requests.get(request_url, timeout=10)
    game_data = request.json()
    return create_game_card_html(game_data, request_url)


def create_game_image_grid(ids: list[int], base_url: str) -> str:
    """
    Create a grid of the web cards that contain the Games in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of the IDs of the games to create the cards.

    Returns:
            ``str``: The string that defines the HTML code of the grid.

    """
    divs_containers = ""
    for id in ids:
        divs_containers += create_game_web_card_to_website(base_url, id)
    return divs_containers
