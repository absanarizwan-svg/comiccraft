from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    app_name: str = "ComicCraft"

    debug: bool = True

    # Google Gemini
    gemini_api_key: str = ""

    gemini_outline_model: str = "gemini-2.5-flash"

    gemini_story_model: str = "gemini-2.5-pro"

    # Hugging Face
    hf_token: str = ""

    hf_image_model: str = (
        "stabilityai/stable-diffusion-xl-base-1.0"
    )

    hf_provider: str = "auto"

    # IMPORTANT:
    # False = use real AI image generation
    demo_mode: bool = False

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()