import requests

from src.website_elements.create_character_card_web import (
    create_character_web_card_to_website,
)


def create_alter_ego_web_card_to_website(
    base_url: str, character_id: int, alter_egos_ids: list[int]
) -> str:
    alter_ego_containers = ""
    for id in alter_egos_ids:
        request_url = f"{base_url}api/characters/{character_id}/alteregos/{id + 1}"
        print(str(request_url))
        request = requests.get(request_url)
        request_alter_ego_json = request.json()
        alter_ego_name = request_alter_ego_json["name"]
        alter_ego_image = request_alter_ego_json["images"][0]

        alter_ego_containers += f"""<div class="alter_ego_container">
        <a href="{str(request_url)}" class="alter_ego_link">
        <img src="{alter_ego_image}"/>
        <p class="alter_ego_name">
        {alter_ego_name}
        </p>
        </a>
        </div>\n
        """

    html_response = f"""
                <div class="character_and_alterego_grid" >
                {create_character_web_card_to_website(base_url, character_id)}
                <div class="alter_egos_container"> 
                {alter_ego_containers}
                </div>
                </div>
                """

    return html_response


def create_alter_ego_image_grid(ids: list[list[int]], base_url: str) -> str:
    divs_containers = ""
    for character in ids:
        character_id = character[0]
        alter_ego_id = character[1:]
        divs_containers += create_alter_ego_web_card_to_website(
            base_url, character_id, alter_ego_id
        )
    return divs_containers
