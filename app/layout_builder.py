from typing import List

from app.schemas import PanelStory


def build_comic_layout(
    panels: List[PanelStory],
    image_paths: List[str]
) -> list[dict]:

    layout = []

    for panel, image_path in zip(panels, image_paths):
        item = panel.model_dump()
        item["image_path"] = image_path
        layout.append(item)

    return layout