from fastapi import Request
from fastapi.responses import JSONResponse
from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_footer_web import create_footer
from src.website_elements.create_404_iamge_web import get_404_image


async def custom_404_handler(request: Request, exc):
    path = request.url.path

    if path.startswith("/api/"):
        return JSONResponse(status_code=404, content={"error": "Not Found"})

    else:
        return templates.TemplateResponse(
            "404.html",
            context={
                "request": request,
                "image_404": f'<img id="Not_Found_Image" src="{get_404_image()}">',
                "footer": create_footer(),
            },
            status_code=404,
        )
