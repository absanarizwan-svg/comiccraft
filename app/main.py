from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"


(STATIC_DIR / "panels").mkdir(parents=True, exist_ok=True)
(STATIC_DIR / "exports").mkdir(parents=True, exist_ok=True)
(STATIC_DIR / "generated").mkdir(parents=True, exist_ok=True)


app = FastAPI(
    title="ComicCraft - AI Comic Story Creator",
    version="1.0.0",
    description=(
        "AI-powered comic story creator "
        "using Gemini and Hugging Face."
    ),
)


app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


app.include_router(router)


@app.get("/health", tags=["system"])
async def health():
    return {
        "status": "ok",
        "service": "ComicCraft",
    }