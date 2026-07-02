from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser
from app.services.scene_mapper import SceneMapper

class ScreenplayAgent:
    """Generates screenplay JSON from a story."""

    def __init__(self):
        self.ollama = OllamaService()

    def generate_screenplay(self, story: str):

        prompt = FileManager.read_text(
            "app/prompts/screenplay_prompt.txt"
        )

        prompt = prompt.format(story=story)
        response = self.ollama.generate(prompt)

        print("\n========== RAW AI RESPONSE ==========\n")
        print(response)
        print("\n=====================================\n")

        screenplay_dict = JsonParser.parse(response)

        screenplay = SceneMapper.from_dict(screenplay_dict)

        filename = FileManager.generate_filename(
            "screenplays",
            "screenplay"
        ).replace(".txt", ".json")

        FileManager.write_json(filename, screenplay_dict)

        return screenplay, filename