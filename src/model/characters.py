from pydantic import BaseModel
from typing import List


class Character(BaseModel):
    id: int
    name: str
    friend_group: int
    family: int
    birthday: str
    age: int
    religion: List[str]
    images: list[str]
    first_apperance: dict
    alter_egos: dict
    famious_guest: bool
