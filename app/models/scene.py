from dataclasses import dataclass
from typing import List


@dataclass
class Scene:
    scene_number: int
    title: str
    narration: str
    characters: List[str]
    environment: str
    actions: str
    emotion: str
    camera: str
    lighting: str
    duration: int