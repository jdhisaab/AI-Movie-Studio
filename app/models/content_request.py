from dataclasses import dataclass


@dataclass
class ContentRequest:
    """Input request shared by all AI agents."""

    genre: str
    language: str
    duration: int
    platform: str
    style: str