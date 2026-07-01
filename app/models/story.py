from dataclasses import dataclass
from datetime import datetime


@dataclass
class Story:
    """Represents a generated story."""

    title: str
    genre: str
    language: str
    content: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")