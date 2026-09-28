from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from fpdf import FPDF


BASE_DIR = Path(__file__).resolve().parent.parent
EXPORT_DIR = BASE_DIR / "static" / "exports"


def local_image_path(image_path: str) -> Path | None:
    parsed = urlparse(image_path)
    relative_path = parsed.path.lstrip("/")

    path = BASE_DIR / relative_path

    if path.exists():
        return path

    return None


def save_pdf(comic_id: str, layout: list[dict]) -> str:
    EXPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        f"comiccraft-{comic_id}-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.pdf"
    )

    output = EXPORT_DIR / filename

    pdf = FPDF()
    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for panel in layout:
        pdf.add_page()

        pdf.set_font(
            "Helvetica",
            "B",
            18
        )

        pdf.multi_cell(
            0,
            10,
            f"Panel {panel['panel_number']}: "
            f"{panel['title']}"
        )

        pdf.ln(3)

        image_path = local_image_path(
            panel["image_path"]
        )

        if image_path:
            try:
                if image_path.suffix.lower() in (
                    ".png",
                    ".jpg",
                    ".jpeg"
                ):
                    pdf.image(
                        str(image_path),
                        x=15,
                        w=180
                    )
                    pdf.ln(5)
            except Exception:
                pass

        pdf.set_font(
            "Helvetica",
            "I",
            11
        )

        pdf.multi_cell(
            0,
            7,
            panel["scene_description"]
        )

        pdf.ln(3)

        pdf.set_font(
            "Helvetica",
            "B",
            12
        )

        pdf.multi_cell(
            0,
            7,
            f"Caption: {panel['caption']}"
        )

        pdf.ln(2)

        pdf.set_font(
            "Helvetica",
            "",
            11
        )

        pdf.multi_cell(
            0,
            7,
            panel["narration"]
        )

        pdf.ln(2)

        for dialogue in panel.get(
            "dialogue",
            []
        ):
            pdf.set_font(
                "Helvetica",
                "B",
                11
            )

            pdf.multi_cell(
                0,
                7,
                f"Dialogue: {dialogue}"
            )

    pdf.output(str(output))

    return f"/static/exports/{filename}"