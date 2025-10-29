import requests


def create_album_web_card_to_website(base_url: str, album_id: int) -> str:
    request_url = f"{base_url}api/albums/{album_id}"
    request = requests.get(request_url)
    request_album_json = request.json()

    album_name = request_album_json["name"]
    album_release = request_album_json["release_date"]

    album_cover = request_album_json["web_album_cover"]

    album_url = request_album_json["album_url"]

    html_button = (
        """
        <div class="album_not_avalible_button">
        Not Avalible
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
    print(html_button)
    html_response = f"""
        <div class="album_card" >
                <a href="{request_url}" target="blanck" class="album_card_link">
                                <img class="album_image" src="{album_cover}" alt="Cover">
                                <p class="album_name">
                                        <b>{album_name}</b>
                                </p>
                                        <p class="album_release">
                                        Release Date: {album_release}
                                </p>
                </a>\n
                {html_button}
        </div>
        """
    return html_response


def create_album_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_album_web_card_to_website(base_url, id)
    return divs_containers
