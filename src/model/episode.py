# UPDATED

from pydantic import BaseModel


class Episode(BaseModel):
    id: int
    name: str
    episode_numbering: dict
    realese_date: str
    description: str
    episode_in_website: dict
