import requests


def create_character_web_card_to_website(base_url: str, character_id: int) -> str:
    request_url = f"{base_url}api/characters/{character_id}"
    request = requests.get(request_url)

    request_json = request.json()

    character_name = request_json["name"]
    character_image = request_json["images"][0]
    character_birthday = (
        request_json["birthday"] if request_json["birthday"] is not None else "Unknown"
    )
    character_age = (
        request_json["age"] if request_json["age"] is not None else "Unknown"
    )
    character_debut_episode = request_json["first_apperance"]["name"]
    html_response = f"""
        <a href="{request_url}" target="blanck" class="character_card_link">
        <div class="character_card" >
        <div class="character_background">
        <img class="character_image" src="{character_image}" alt="Avatar">
        </div>
        <p class="character_name">
        <b>{character_name}</b> 
        <b>age: {character_age}</b>
        </p>
        <p class="character_description">Birthday: {character_birthday}</p>
        <p class="character_description">Debut:       {character_debut_episode}</p>
        </div>
        </a>\n
        """
    return html_response


def create_character_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_character_web_card_to_website(base_url, id)
    return divs_containers
