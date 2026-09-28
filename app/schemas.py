from typing import List
from pydantic import BaseModel, Field, field_validator


class PromptRequest(BaseModel):
    story_prompt: str = Field(..., min_length=5, max_length=1500)
    character_name: str = Field(..., min_length=1, max_length=80)
    setting: str = Field(..., min_length=1, max_length=120)
    tone: str = Field(..., min_length=1, max_length=50)
    art_style: str = Field(..., min_length=1, max_length=80)

    @field_validator(
        "story_prompt",
        "character_name",
        "setting",
        "tone",
        "art_style"
    )
    @classmethod
    def clean_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("This field cannot be empty.")

        return value


class PanelOutline(BaseModel):
    panel_number: int
    title: str
    scene_description: str
    image_prompt: str


class PanelStory(BaseModel):
    panel_number: int
    title: str
    scene_description: str
    caption: str
    narration: str
    dialogue: List[str] = Field(default_factory=list)
    image_prompt: str


class ComicResponse(BaseModel):
    comic_id: str
    panels: List[PanelStory]
    pdf_url: str