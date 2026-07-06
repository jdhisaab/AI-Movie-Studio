from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class ImagePromptAgent:

    def __init__(self):
        self.ollama = OllamaService()

    def generate_prompt(self, scene: str):

        prompt = FileManager.read_text(
            "app/prompts/image_prompt.txt"
        )

        prompt = prompt.format(scene=scene)

        response = self.ollama.generate(prompt)

        return JsonParser.parse(response)