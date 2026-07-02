from app.services.ollama_service import OllamaService
from app.services.narration_mapper import NarrationMapper
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class NarrationAgent:

    def __init__(self):
        self.ollama = OllamaService()

    def generate_narration(self, screenplay):

        prompt_template = FileManager.read_text(
            "app/prompts/narration_prompt.txt"
        )

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Title: {scene.title}

Narration: {scene.narration}

Actions: {scene.actions}
"""

        prompt = prompt_template.format(
            screenplay=screenplay_text
        )

        response = self.ollama.generate(prompt)

        data = JsonParser.parse(response)

        narrations = NarrationMapper.from_dict(data)

        return narrations