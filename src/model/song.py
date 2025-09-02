from pydantic import BaseModel
from typing import Optional


class Song(BaseModel):
    id: int
    name: str
    album_number: Optional[int] = None
    lyrics: str
    song_url: str
