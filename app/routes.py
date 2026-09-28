from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.schemas import PromptRequest
from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

router = APIRouter()

COMICS = {}


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/generate")
async def generate_comic(request: Request):

    try:
        form = await request.form()

        story_prompt = str(
            form.get("story_prompt", "")
        ).strip()

        character_name = str(
            form.get("character_name", "")
        ).strip()

        setting = str(
            form.get("setting", "")
        ).strip()

        tone = str(
            form.get("tone", "")
        ).strip()

        art_style = str(
            form.get("art_style", "")
        ).strip()

        prompt_request = PromptRequest(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style,
        )

        outline = generate_outline(prompt_request)

        panels = generate_story(
            prompt_request,
            outline
        )

        image_paths = []

        for panel in panels:
            image_path = generate_image(
                panel.image_prompt,
                panel.panel_number,
                panel.title,
            )

            image_paths.append(image_path)

        layout = build_comic_layout(
            panels,
            image_paths
        )

        comic_id = uuid4().hex[:8]

        pdf_url = save_pdf(
            comic_id,
            layout
        )

        COMICS[comic_id] = {
            "comic_id": comic_id,
            "panels": panels,
            "layout": layout,
            "pdf_url": pdf_url,
        }

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "comic_id": comic_id,
                "panels": panels,
                "layout": layout,
                "pdf_url": pdf_url,
            },
        )

    except Exception as error:

        print("GENERATE ERROR:", repr(error))

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "error": f"Generate error: {error}"
            },
            status_code=500,
        )