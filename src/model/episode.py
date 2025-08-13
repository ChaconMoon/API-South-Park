# UPDATED

from pydantic import BaseModel


class Episode(BaseModel):
    id: int
    name: str
    sesaon: int
    episode: int
    realese_date: str
    description: str
    view_on_website: str
