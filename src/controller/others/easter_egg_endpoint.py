from fastapi import APIRouter, Request, Response

from src.controller.others.easter_egg_controller import get_easter_egg

router = APIRouter(tags=["Others"])


@router.get("/api/easteregg/{name}", tags=["Others"])
def return_easter_egg(name: str, request: Request, response: Response):
    base_url = str(request.base_url)
    return get_easter_egg(name=name, base_url=base_url)
