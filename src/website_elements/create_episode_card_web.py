import requests


def create_episode_web_card_to_website(base_url: str, episode_id: int) -> str:
    request_url = f"{base_url}api/episode/{episode_id}"
    request = requests.get(request_url)

    request_json = request.json()
    print(request_url)
    print(request_json)

    episode_name = request_json["name"]
    episode_image = request_json["episode_thumbnail"]
    episode_release_date = request_json["realese_date"]
    episode_description = request_json["description"]
    episode_status = request_json["episode_in_website"]["status"]
    episode_url = request_json["episode_in_website"]["website_url"]

    html_response = f"""
        <a href="{request_url}" class="episode_card_link">
        <div class="episode_card">
        <img class="episode_image" src="{episode_image}" alt="Avatar">
        <p class="episode_number">
        <b>Episode: {episode_id}</b>
        </p>
        <p class="episode_name">
        <b>Name: {episode_name}</b> 
        </p>
        <div class="episode_description">
        <p class="episode_description_text">
        <b>{episode_description}</b>
        </p>
        <p class="episode_status">STATUS: {episode_status}</p>
        <p class="episode_release">{episode_release_date}</p>
        </div>
        </div>
        </a>\n
        """
    return html_response


def create_episode_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_episode_web_card_to_website(base_url, id)
    return divs_containers
