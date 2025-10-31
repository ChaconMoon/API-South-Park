from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from markdown import markdown
from src.controller.structure.web_templates_controller import templates
from src.website_elements.create_footer_web import create_footer
from src.website_elements.create_post_card_grid import (
    create_blog_links,
    create_post_grid_in_blog,
    get_blog_last_index,
    get_intro_in_menu,
    get_social_media_thumbnail_in_menu,
    get_title_in_menu,
)

router = APIRouter(tags=["Blog"])


@router.get("/blog/article/{entry}", tags="Blog")
def show_blog(request: Request, response: Response, entry: str):
    try:
        with open(f"./website/posts/{entry}.MD", encoding="utf-8") as f:
            markdown_content = f.read()
        html_blog_entry = markdown(
            markdown_content,
            extensions=["fenced_code", "tables", "attr_list", "md_in_html"],
        )
        html_blog_entry = html_blog_entry.replace("<p><img", "<img")
        html_blog_entry = html_blog_entry.replace('webp" /></p>', 'webp" />')
    except FileNotFoundError as e:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse(
        "blog_page_post.html",
        context={
            "request": request,
            "blog_item": html_blog_entry,
            "base_url": request.base_url,
            "articule_title_in_social_media": get_title_in_menu(f"{entry}.MD"),
            "articule_description_in_social_media": get_intro_in_menu(f"{entry}.MD"),
            "image_in_social_media": f"{str(request.base_url)[:-1].replace('http://', 'https://')}{get_social_media_thumbnail_in_menu(f'{entry}.MD')}",
            "url_in_social_media": f"{str(request.base_url).replace('http://', 'https://')}blog/article/{entry}",
            "footer": create_footer(),
        },
    )


@router.get("/blog/{index}", tags="blog")
def show_posts_grid(request: Request, response: Response, index: int):
    grid_elements = create_post_grid_in_blog(
        start_index=index, base_url=request.base_url
    )
    print(grid_elements)
    if grid_elements != "":
        return templates.TemplateResponse(
            "blog_page.html",
            context={
                "request": request,
                "base_url": request.base_url,
                "blog_posts_grid": grid_elements,
                "blog_links": create_blog_links(),
                "footer": create_footer(),
            },
        )
    else:
        return RedirectResponse(f"/blog/{get_blog_last_index()}")
