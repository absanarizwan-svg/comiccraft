from typing import List

from app.schemas import PanelOutline, PanelStory, PromptRequest


def generate_story(
    request: PromptRequest,
    outline: List[PanelOutline]
) -> List[PanelStory]:

    captions = [
        "A new adventure begins...",
        "A mysterious clue changes everything.",
        "The moment of truth arrives.",
        "One clever idea changes the situation.",
        "Every ending can become a new beginning.",
    ]

    dialogues = [
        [
            f"{request.character_name}: Something tells me this adventure is just beginning!"
        ],
        [
            f"{request.character_name}: What could this clue mean?"
        ],
        [
            f"{request.character_name}: I can solve this. I just need to think differently."
        ],
        [
            f"{request.character_name}: That's it! The answer was right in front of me."
        ],
        [
            f"{request.character_name}: What an adventure!"
        ],
    ]

    result = []

    for index, panel in enumerate(outline):
        result.append(
            PanelStory(
                panel_number=panel.panel_number,
                title=panel.title,
                scene_description=panel.scene_description,
                caption=captions[index],
                narration=(
                    f"{request.character_name} continues the adventure "
                    f"in {request.setting} with a {request.tone.lower()} spirit."
                ),
                dialogue=dialogues[index],
                image_prompt=panel.image_prompt,
            )
        )

    return result