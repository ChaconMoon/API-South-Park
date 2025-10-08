import requests


def create_song_web_card_to_website(base_url: str, song_id: int) -> str:
    song_request_url = f"{base_url}api/song/{song_id}"
    request = requests.get(song_request_url)

    request_json = request.json()

    song_name = request_json["name"]
    album_number = int(request_json["album_number"])
    song_url = request_json["song_url"]

    request_url = f"{base_url}api/album/{album_number}"
    request = requests.get(request_url)
    request_album_json = request.json()

    album_name = request_album_json["name"]
    album_release = request_album_json["release_date"]

    album_cover = request_album_json["album_cover"]

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
    print(html_button)
    html_response = f"""
        <div class="song_card" >
                <a href="{song_request_url}" class="song_card_link">
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
    divs_containers = ""
    for id in ids:
        divs_containers += create_song_web_card_to_website(base_url, id)
    return divs_containers
