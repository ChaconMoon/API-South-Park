# UPDATED

from pydantic import BaseModel


class Family(BaseModel):
    id: int
    name: str
    images: list[str]
