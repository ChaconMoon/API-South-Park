import json
import re


def create_post_grid_in_blog(start_index: int, base_url=str):
    divcontainer = ""
    markdown_files = []
    post_dict: dict = {}
    size_per_page = 6
    if start_index == 1:
        index = 0
    else:
        index = (start_index - 1) * size_per_page
    with open("data/post_order.json") as file:
        post_dict = json.load(file)

    markdown_files = list(post_dict.items())[index : index + size_per_page]

    for index in range(0, len(markdown_files), 1):
        divcontainer += f"""<a href="{base_url}blog/article/{str(markdown_files[index][1]).strip(".MD")}">
        <div class="post_in_menu">
        <img class="post_thumbnail" src="{get_thumbnail_in_menu(str(markdown_files[index][1]))}">
        <h3>{get_title_in_menu(str(markdown_files[index][1]))}</h3>
        <p class="post_intro">{get_intro_in_menu(str(markdown_files[index][1]))}</p>
        </div>
        </a>"""
    return divcontainer


#
# AI CODE
#


def get_thumbnail_in_menu(file_nmae: str):
    try:
        with open(f"website/posts/{file_nmae}") as file:
            return str(re.search(r"(/blog/images/[^)]*)(?=\))", file.readline())[0])
    except FileNotFoundError as e:
        return "/blog/images/Article_Not_Found.webp"


def get_title_in_menu(file_nmae: str):
    try:
        with open(f"website/posts/{file_nmae}") as file:
            file.readline()
            return str(re.search(r"^#\s*(.+?)(?=\s*\{|\s*$)", file.readline()).group(1))
    except FileNotFoundError as e:
        return f"NOT FOUND: {file_nmae}"


def get_intro_in_menu(file_nmae: str):
    try:
        with open(f"website/posts/{file_nmae}") as file:
            file.readline()
            file.readline()
            rest = file.read()
            # eliminar texto entre llaves {...}
            cleaned = re.sub(r"\{[^}]*\}", "", rest)
            # normalizar espacios y recortar
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            return cleaned[:300] + "..." if cleaned else ""
    except FileNotFoundError as e:
        return f"The file {file_nmae} wasn't found, please create the article or delete it from the list"


#
# END AI CODE
#


def create_blog_links():
    link_list = ""

    pages = get_blog_last_index()

    for page in range(1, pages + 1, 1):
        link_list += f"""<a class="blog_link" href="/blog/{page}">{page}</a>"""
    return link_list


def get_blog_last_index():
    lines = sum(1 for line in open("data/post_order.json"))
    pages = int(lines / 6)

    if lines % 6 != 0:
        pages += 1
    return pages
