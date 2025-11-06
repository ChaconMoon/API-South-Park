"""
Module written by Carlos Chacón.

This Module defines the functions to create post cards for the Dev Blog website.
Each function handles different aspects of post card generation and grid layout.
"""

import logging
import re

import toon


def create_post_grid_in_blog(start_index: int, base_url=str) -> str:
    """
    Create a grid of post cards for the Dev Blog website.

    Params:
        start_index: The page number to start displaying posts from
        base_url: The base URL used to create the blog post links

    Returns:
        str: HTML string containing the grid of blog post cards

    """
    divcontainer = ""
    markdown_files = []
    size_per_page = 6
    if start_index == 1:
        index = 0
    else:
        index = (start_index - 1) * size_per_page
    with open("data/post_order.toon") as file:
        toon_file = toon.decode(file.read())
        logging.info(toon_file["posts"])

    markdown_files = toon_file["posts"][index : index + size_per_page]

    for index in range(0, len(markdown_files), 1):
        divcontainer += f"""
        <a href="{base_url}blog/article/{str(markdown_files[index]).removesuffix(".MD")}">
        <div class="post_in_menu">
        <img class="post_thumbnail"
         src="{get_thumbnail_in_menu(str(markdown_files[index]))}">
        <h3>{get_title_in_menu(str(markdown_files[index]))}</h3>
        <p class="post_intro">{get_intro_in_menu(str(markdown_files[index]))}</p>
        </div>
        </a>"""  # Fixed URL, delete the M, D, . at the start.
    return divcontainer


def get_thumbnail_in_menu(file_name: str) -> str:
    """
    Extract the thumbnail image path from a blog post file.

    Params:
        file_name: Name of the markdown file to process

    Returns:
        str: Path to the thumbnail image or default image if file not found

    """
    try:
        with open(f"website/posts/{file_name}") as file:
            return str(re.search(r"(/blog/images/[^)]*)(?=\))", file.readline())[0])
    except FileNotFoundError:
        return "/blog/images/Article_Not_Found.webp"


def get_title_in_menu(file_name: str) -> str:
    """
    Extract the title from a blog post file.

    Params:
        file_name: Name of the markdown file to process

    Returns:
        str: Title of the blog post or error message if file not found

    """
    try:
        with open(f"website/posts/{file_name}") as file:
            file.readline()
            return str(re.search(r"^#\s*(.+?)(?=\s*\{|\s*$)", file.readline()).group(1))
    except FileNotFoundError:
        return f"NOT FOUND: {file_name}"


def get_intro_in_menu(file_name: str) -> str:
    """
    Extract and format the introduction text from a blog post file.

    Params:
        file_name: Name of the markdown file to process

    Returns:
        str: First 300 characters of the post content or error message if file not found

    """
    try:
        with open(f"website/posts/{file_name}") as file:
            file.readline()
            file.readline()
            rest = file.read()
            # eliminar texto entre llaves {...}
            cleaned = re.sub(r"\{[^}]*\}", "", rest)
            # normalizar espacios y recortar
            cleaned = re.sub(r"\s+", " ", cleaned).strip()
            return cleaned[:300] + "..." if cleaned else ""
    except FileNotFoundError:
        return f"""The file {file_name} wasn't found,
         please create the article or delete it from the list"""


def create_blog_links() -> str:
    """
    Create pagination links for the blog pages.

    Returns:
        str: HTML string containing numbered links for blog navigation

    """
    link_list = ""

    pages = get_blog_last_index()
    for page in range(0, pages, 1):
        link_list += f"""<a class="blog_link" href="/blog/{page + 1}">{page + 1}</a>"""
    return link_list


def get_blog_last_index() -> int:
    """
    Calculate the total number of blog pages based on post count.

    Returns:
        int: Total number of pages needed to display all posts

    """
    lines = sum(1 for _ in open("data/post_order.toon")) - 1  # The start line
    pages = int(lines / 6)

    if lines % 6 != 0:
        pages += 1
    return pages


def get_social_media_thumbnail_in_menu(file_name: str) -> str:
    """
    Extract and convert the thumbnail path for social media usage.

    Params:
        file_name: Name of the markdown file to process

    Returns:
        str: Path to the social media version of the thumbnail
         or default image if file not found

    """
    try:
        with open(f"website/posts/{file_name}") as file:
            return str(
                re.search(r"(/blog/images/[^)]*)(?=\))", file.readline())[0].replace(
                    "/blog/images/", "/blog/social_media/images/"
                )
            ).replace(".webp", ".jpg")
    except FileNotFoundError:
        return "/blog/images/Article_Not_Found.webp"
