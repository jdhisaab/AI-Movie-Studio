from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager


class ScreenplayAgent:
    """Generates a screenplay from a story."""

    def __init__(self):
        self.ollama = OllamaService()

    def generate_screenplay(self, story: str) -> str:
        prompt = FileManager.read_text(
            "app/prompts/screenplay_prompt.txt"
        )

        prompt = prompt.format(story=story)

        screenplay = self.ollama.generate(prompt)

        file_name = FileManager.generate_filename("screenplays", "screenplay")

        FileManager.write_text(file_name, screenplay)

        return file_name