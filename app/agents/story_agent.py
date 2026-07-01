from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager


class StoryAgent:
    """Agent responsible for generating cinematic stories."""

    def __init__(self):
        self.ollama = OllamaService()

    def generate_story(
        self,
        genre: str,
        language: str,
        duration: int
    ) -> str:

        prompt = FileManager.read_text(
            "app/prompts/story_prompt.txt"
        )

        prompt = prompt.format(
            genre=genre,
            language=language,
            duration=duration
        )

        story = self.ollama.generate(prompt)

        file_name = FileManager.generate_filename("stories", "story")

        FileManager.write_text(file_name, story)

        return file_name