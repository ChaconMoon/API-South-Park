"""
Module writted by Carlos Chacón.

This module defines the enums used in the EasterEgg endpoints
"""

from enum import Enum


class EasterEggType(Enum):
    """
    Enumeration of possible easter egg response types.

    Values:
        NONE (0): No easter egg found
        CHARACTERS (1): Return character-based easter egg
        EPISODES (2): Return episode-based easter egg
        CUSTOM (3): Return custom json response easter egg

    """

    NONE = 0
    CHARACTERS = 1
    EPISODES = 2
    CUSTOM = 3


class EasterEggName(Enum):
    """
    Enumeration of the available easteregg with their ID.

    Values:
        IHAVEDIABETES (0): Returns the two kids of the school that have diabetes:
        (Scott Malkinson and Sophie Gray)

        THEWHITEHOUSE (1): Returns all the characters that are
        in the White House at the moment
    """

    IHAVEDIABETES = 0
    THEWHITEHOUSE = 1
    THEEPSTEINFILES = 2
    # OTHER = 2
