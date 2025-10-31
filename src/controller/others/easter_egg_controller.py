from enum import Enum

from src.controller.characters.characters_controller import get_character_list


class EasterEggType(Enum):
    NONE = 0
    CHARACTERS = 1
    EPISODES = 2
    CUSTOM = 3


def get_easter_egg(name: str, base_url: str):
    items = list()
    type = EasterEggType.NONE
    match name.lower():
        case "ihavediabetes":
            items = [141, 107]
            type = EasterEggType.CHARACTERS

    print(items)
    print(type.value)
    match type:
        case EasterEggType.CHARACTERS:
            return get_character_list(ids=items, base_url=base_url)

        case EasterEggType.EPISODES:
            pass
        case EasterEggType.CUSTOM:
            pass
    return {"message": "No Easter Egg Found"}
