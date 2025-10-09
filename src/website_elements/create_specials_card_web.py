import requests


def create_special_web_card_to_website(base_url: str, album_id: int) -> str:
    request_url = f"{base_url}api/special/{album_id}"
    request = requests.get(request_url)
    request_album_json = request.json()

    title = request_album_json["title"]
    release_date = request_album_json["release_date"]

    description = request_album_json["description"]

    poster_special = request_album_json["poster"]

    link = request_album_json["link"]

    html_response = f"""
        <a href="{request_url}" class="special_card_link">
                <div class="special_card" >
                                <img class="special_poster" src="{poster_special}" alt="Cover">
                                <p class="special_name">
                                        <b>{title}</b>
                                </p>
                                
                                <p class="release_date">
                                        Release Date: {release_date}
                                </p>

                                <p class="special_description">
                                        {description}
                                </p>
                                
                </div>
        </a>\n
        """
    return html_response


def create_special_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    index = 0
    for id in ids:
        if index in [0, 2]:
            divs_containers += """<div class="special_grid2"> """
        elif index == 4:
            divs_containers += """<div class="special_grid3"> """
        divs_containers += create_special_web_card_to_website(base_url, id)

        if index in [1, 3, 6]:
            divs_containers += """</div>"""
        index += 1
    return divs_containers
