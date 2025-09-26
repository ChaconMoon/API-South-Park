import requests


def create_character_web_card_to_website(base_url: str, character_id: int) -> str:
    request_url = f"{base_url}api/character/{character_id}"
    request = requests.get(request_url)

    request_json = request.json()
    print(request_url)
    print(request_json)

    character_name = request_json["character"]["name"]
    character_image = request_json["character"]["images"][0]
    character_birthday = (
        request_json["character"]["birthday"]
        if request_json["character"]["birthday"] is not None
        else "Unknown"
    )
    character_age = (
        request_json["character"]["age"]
        if request_json["character"]["age"] is not None
        else "Unknown"
    )
    character_debut_episode = request_json["character"]["first_apperance"]["name"]
    html_response = f"""
        <a href="{request_url}" class="card_link">
        <div class="character_card" >
        <div class="character_background">
        <img class="character_image" src="{character_image}" alt="Avatar">
        </div>
        <p class="character_name">
        <b>{character_name}</b> 
        <b>age: {character_age}</b>
        </p>
        <p class="description">Birthday: {character_birthday}</p>
        <p class="description">Debut:       {character_debut_episode}</p>
        </div>
        </a>\n
        """
    return html_response


def create_character_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_character_web_card_to_website(base_url, id)
    return divs_containers
