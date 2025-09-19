import requests


def create_character_web_card_to_website(base_url: str, character_id: int) -> str:
    request_url = f"{base_url}api/character/{character_id}"
    request = requests.get(request_url)

    request_json = request.json()
    print(request_url)
    print(request_json)

    character_name = request_json["character"]["name"]
    character_image = request_json["character"]["images"][0]
    character_birthday = request_json["character"]["birthday"]
    character_age = request_json["character"]["age"]
    html_response = f"""
        <div class="character_card" style="width:30vw;flex: 1 0 21%">
        <img src="{character_image}" alt="Avatar" style="height:30vh;padding-left:40;padding-right:auto;" align="center">
        <h4><b>{character_name} age: {character_age}</b></h4>
        <p>birthday: {character_birthday}</p>
        <p>Json: <a href="{request_url}">{request_url}</a><p>
        </div>\n
        """
    return html_response


def create_character_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_character_web_card_to_website(base_url, id)
    return divs_containers
