from fastapi import APIRouter, Request, Response

from src.controller.chipokomon.chinpokomon_controller import get_chinpokomon_by_id

router = APIRouter(tags=["Chinpokomon"])


@router.get("/api/chinpokomon/{id}")
def get_chinpokomon(id: int, request: Request, response: Response):
    base_url = str(request.base_url)
    return get_chinpokomon_by_id(id=id, base_url=base_url)
