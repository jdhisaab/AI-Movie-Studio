from dataclasses import dataclass


@dataclass
class ImagePrompt:
    """Represents one AI image prompt."""

    scene_number: int
    positive_prompt: str
    negative_prompt: str