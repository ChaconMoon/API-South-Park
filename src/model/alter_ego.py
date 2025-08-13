from pydantic import BaseModel


class AlterEgo(BaseModel):
    id: int
    original_character: str
    name: str
    images: list[str]
