from dataclasses import dataclass


@dataclass
class ContentResponse:
    """Output shared by AI agents."""

    title: str
    summary: str
    story: str