from typing import TypedDict


class MovieState(TypedDict):

    genre: str
    language: str
    duration: int

    story: str

    screenplay: object

    image_prompts: list

    images: list

    audio: str

    video: str