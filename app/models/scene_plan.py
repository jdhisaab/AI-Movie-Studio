from pydantic import BaseModel


class ScenePlan(BaseModel):

    scene_number: int

    location: str

    time_of_day: str

    camera_motion: str

    character_motion: str

    background_motion: str

    visual_effects: list[str]

    style: str

    aspect_ratio: str