from dataclasses import dataclass
from datetime import datetime


@dataclass
class Story:
    title: str
    genre: str
    language: str
    duration: int
    content: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")