import os
import re
from pathlib import Path

from huggingface_hub import InferenceClient

from app.config import get_settings


BASE_DIR = Path(__file__).resolve().parent.parent
PANELS_DIR = BASE_DIR / "static" / "panels"


def safe_name(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", value)
    value = value.strip("-").lower()
    return value[:80] or "panel"


def generate_image(
    image_prompt: str,
    panel_number: int,
    title: str
) -> str:

    settings = get_settings()

    PANELS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        f"panel-{panel_number}-"
        f"{safe_name(title)}.png"
    )

    output_path = PANELS_DIR / filename

    hf_token = settings.hf_token or os.getenv("HF_TOKEN")

    if not hf_token:
        raise RuntimeError(
            "HF_TOKEN is missing in the .env file."
        )

    client = InferenceClient(
        api_key=hf_token,
        provider="auto"
    )

    prompt = f"""
Create one colorful cartoon comic panel.

{image_prompt}

Style: colorful cartoon comic.
Show one clear scene.
Clean line art.
Friendly expressions.
Simple detailed background.
Landscape composition.
"""

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    image.save(output_path)

    return f"/static/panels/{filename}"