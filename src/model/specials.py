from pydantic import BaseModel


class Special(BaseModel):
    id: int
    title: str
    release_date: str
    description: str
    link: str
