"""
Module written by Carlos Chacón.

This Module defines the creator functions to generate random 404 error images
in the index website.
"""

import random


def get_404_image() -> str:
    """
    Generate a random 404 error image path from available options.

    Returns:
            ``str``: The string containing the path to a random 404 image.

    """
    number_random = random.randrange(1, 101)  # noqa: S311 No Safe Generation (Evaluate correct it)

    match number_random:
        case number_random if number_random < 34:
            return "/img/website/Cartel_NOT_FOUND_Woke_is_Dead.webp"
        case number_random if number_random < 67:
            return "/img/website/Cartel_NOT_FOUND_Azizam.webp"
        case number_random if number_random < 100:
            return "/img/website/Cartel_NOT_FOUND_Normal.webp"
        case _:
            return "/img/website/Cartel_NOT_FOUND_Charlie_Brown.webp"
