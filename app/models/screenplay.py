from dataclasses import dataclass
from typing import List

from app.models.scene import Scene


@dataclass
class Screenplay:
    """Represents a complete screenplay."""

    title: str
    scenes: List[Scene]