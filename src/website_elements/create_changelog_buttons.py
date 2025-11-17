"""
Module written by Carlos Chacón.

This module contains the fuction that creates de buttons to move in the Changelog
"""

import logging

import toon


def create_changelog_links(actual_post) -> str:
    """
    Create pagination links for the blog pages.

    Returns:
        str: HTML string containing numbered links for blog navigation

    """
    link_list = ""

    with open("data/changelog_order.toon") as file:
        toon_file = toon.decode(file.read())
        logging.info(toon_file["posts"])

    if len(toon_file["posts"]) == 1:
        return ""

    try:
        posts = toon_file["posts"]
        idx = posts.index(actual_post)
    except (ValueError, KeyError):
        return ""

    if idx > 0:
        prev = posts[idx - 1].removesuffix(".MD")
        link_list += f"""<a class="endpoint_link" href="/changelog/{prev}">
        « {prev.replace("_", " ")}</a>"""

    if idx < len(posts) - 1:
        if link_list:
            link_list += " "
        nxt = posts[idx + 1].removesuffix(".MD")
        link_list += f"""<a class="endpoint_link" href="/changelog/{nxt}">
        {nxt.replace("_", " ")} »</a>"""

    return link_list
