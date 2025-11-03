"""
Module written by Carlos Chacón.

This Module defines the creator functions to create the web cards of the families
in the index website.
"""

import requests


def create_family_web_card_to_website(base_url: str, family_id: int) -> str:
    """
    Create a web card that contains a Family in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            family_id: The ID of the family to create the card.

    Returns:
            ``str``: The string that defines the HTML code of the card.

    """
    request_url = f"{base_url}api/families/{family_id}"
    request = requests.get(request_url, timeout=10)
    request_json = request.json()

    family_name = request_json["name"]
    family_images = request_json["images"]
    family_members = request_json["members"]

    members_div = "".join(
        f"""<div class="family_member">
        <p> - {member["name"]}</p>
        </div>\n"""
        for member in family_members
    )

    return f"""
        <a href="{request_url}" target="blanck" class="family_card_link">
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


def create_family_image_grid(ids: list[int], base_url: str) -> str:
    """
    Create a grid of the web cards that contain the Families in the Index Website.

    Params:
            base_url: The URL used to create the API Call.
            ids: A list of the IDs of the families to create the cards.

    Returns:
            ``str``: The string that defines the HTML code of the grid.

    """
    return "".join(create_family_web_card_to_website(base_url, id) for id in ids)
