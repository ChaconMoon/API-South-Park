import requests


def create_family_web_card_to_website(base_url: str, family_id: int) -> str:
    request_url = f"{base_url}api/family/{family_id}"
    request = requests.get(request_url)

    request_json = request.json()
    print(request_url)
    print(request_json)

    family_name = request_json["family"]["name"]
    family_images = request_json["family"]["images"]
    family_members = request_json["family"]["members"]

    members_div = ""

    for family_member in family_members:
        members_div += f"""<div class="family_member">
        <p> - {family_member["name"]}</p>
        </div>\n"""

    html_response = f"""
        <a href="{request_url}" class="family_card_link">
                <div class="family_card">
                        <img class="family_image" src="{family_images[0]}" alt="Avatar"/>
                        <p class="family_name">
                                <b>{family_name}</b> 
                        </p>
                                <p class="family_number">
                                        <b>ID: {family_id}</b>
                                </p>
                        <div class="family_members_container">
                        {members_div}
                        </div>
                </div>
        </a>\n
        """
    return html_response


def create_family_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_family_web_card_to_website(base_url, id)
    return divs_containers
