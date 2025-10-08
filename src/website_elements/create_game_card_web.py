import requests


def create_game_web_card_to_website(base_url: str, song_id: int) -> str:
    song_request_url = f"{base_url}api/game/{song_id}"
    request = requests.get(song_request_url)

    request_json = request.json()

    game_name = request_json["name"]
    game_developer = request_json["developer"]
    platforms = request_json["platforms"]
    release_date = request_json["release_date"]
    game_cover = request_json["images"][0]

    platforms_divs = ""

    for platform in platforms:
        match str(platform):
            case "XSeries":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=LqoHSNcZYyaZ&format=png&color=000000">
                        </div>
                         """
            case "Dreamcast":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=60853&format=png&color=000000">
                        </div>
                         """
            case "Web":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=119124&format=png&color=000000">
                        </div>
                         """
            case "XOne":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=sHyMKmljmlSj&format=png&color=000000">
                        </div>
                         """
            case "PC":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=12908&format=png&color=000000">
                        </div>
                         """
            case "X360":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://icons.iconarchive.com/icons/sykonist/console/128/Xbox-360-icon.png">
                        </div>
                         """
            case "PS4":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=08OaSZHbTdVv&format=png&color=000000">
                        </div>
                         """
            case "Escape Room":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=12824&format=png&color=000000">
                        </div>
                         """
            case "PS5":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=J2arZBwbzFfE&format=png&color=000000">
                        </div>
                         """
            case "Switch":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=E3bXXtS09hA1&format=png&color=000000">
                        </div>
                         """
            case "IOS":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=20821&format=png&color=000000">
                        </div>
                         """
            case "PS1":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://images.icon-icons.com/829/PNG/128/Playsystem_icon-icons.com_66601.png">
                        </div>
                         """
            case "Blackberry OS":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=xShzmmrWad9Y&format=png&color=000000">
                        </div>
                         """
            case "N64":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=40979&format=png&color=000000">
                        </div>
                         """
            case "PS3":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=68102&format=png&color=000000">
                        </div>
                         """
            case "PSVita":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=TLejNLu7fP0N&format=png&color=000000">
                        </div>
                         """
            case "GBC":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=p4IZ3gBGGvWo&format=png&color=000000">
                        </div>
                         """
            case "Pinball Machine":
                platforms_divs += """<div class="platform_icon">
                        <img src="https://cdn-icons-png.flaticon.com/512/7960/7960368.png">
                        </div>
                         """
            case _:
                platforms_divs += """<div class="platform_icon">
                        <img src="https://img.icons8.com/?size=100&id=DoFiicbRPzDS&format=png&color=000000">
                        </div>
                         """

    html_response = f"""
        <a href="{song_request_url}" class="game_card_link">
                <div class="game_card" >
                                        <img class="game_image" src="{game_cover}" alt="Cover">
                                        <p class="game_name">
                                                <b>{game_name}</b>
                                        </p>
                                        <p class="game_release_date">
                                                Release Date: {release_date}
                                        </p>
                                                
                                        <div class="platforms_grid">
                                                {platforms_divs}
                                        </div>
                </div>
        </a>\n
        """
    return html_response


def create_game_image_grid(ids: list[int], base_url: str) -> str:
    divs_containers = ""
    for id in ids:
        divs_containers += create_game_web_card_to_website(base_url, id)
    return divs_containers
