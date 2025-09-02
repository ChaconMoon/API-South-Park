from pydantic import BaseModel


class Album(BaseModel):
    id: int
    name: str
    release_date: str
    album_cover: str
    songs: dict
