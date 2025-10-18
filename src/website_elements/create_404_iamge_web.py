import random


def get_404_image() -> str:
    number_random = random.randrange(1, 101)

    match number_random:
        case number_random if number_random in range(1, 34):
            return "/img/website/Cartel_NOT_FOUND_Woke_is_Dead.webp"
        case number_random if number_random in range(34, 67):
            return "/img/website/Cartel_NOT_FOUND_Azizam.webp"
        case number_random if number_random in range(67, 100):
            return "/img/website/Cartel_NOT_FOUND_Normal.webp"
        case _:
            return "/img/website/Cartel_NOT_FOUND_Charlie_Brown.webp"
