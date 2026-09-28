from typing import List
from app.schemas import PanelOutline, PromptRequest


def generate_outline(request: PromptRequest) -> List[PanelOutline]:
    return [
        PanelOutline(
            panel_number=1,
            title="The Beginning",
            scene_description=f"{request.character_name} begins an adventure in {request.setting}.",
            image_prompt=f"{request.character_name} in {request.setting}, {request.art_style} comic style",
        ),
        PanelOutline(
            panel_number=2,
            title="The Discovery",
            scene_description="A mysterious clue appears.",
            image_prompt=f"{request.character_name} discovering a clue, {request.art_style} comic style",
        ),
        PanelOutline(
            panel_number=3,
            title="The Challenge",
            scene_description="A challenge appears.",
            image_prompt=f"{request.character_name} facing a challenge, {request.art_style} comic style",
        ),
        PanelOutline(
            panel_number=4,
            title="The Solution",
            scene_description=f"{request.character_name} finds a clever solution.",
            image_prompt=f"{request.character_name} solving a problem, {request.art_style} comic style",
        ),
        PanelOutline(
            panel_number=5,
            title="The Ending",
            scene_description="The adventure reaches a happy ending.",
            image_prompt=f"{request.character_name} celebrating, {request.art_style} comic style",
        ),
    ]