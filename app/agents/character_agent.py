from app.services.ollama_service import OllamaService
from app.services.character_mapper import CharacterMapper
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class CharacterAgent:

    def __init__(self):
        self.ollama = OllamaService()

    def generate_characters(self, screenplay):

        prompt_template = FileManager.read_text(
            "app/prompts/character_prompt.txt"
        )

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Characters: {", ".join(scene.characters)}

Narration: {scene.narration}

Actions: {scene.actions}
"""

        prompt = prompt_template.format(
            screenplay=screenplay_text
        )

        response = self.ollama.generate(prompt)

        data = JsonParser.parse(response)

        characters = CharacterMapper.from_dict(data)

        return characters