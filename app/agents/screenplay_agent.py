from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JsonParser
from app.services.scene_mapper import SceneMapper
from app.utils.file_manager import FileManager


class ScreenplayAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_screenplay(self, story):

        prompt = self.load_prompt("screenplay_prompt.txt")

        prompt = self.replace_variables(
            prompt,
            {
                "story": story
            }
        )

        response = self.generate(prompt)
        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("==================================\n")

        screenplay_dict = JsonParser.parse(response)

        screenplay = SceneMapper.from_dict(screenplay_dict)

        filename = FileManager.generate_filename(
            "screenplays",
            "screenplay"
        ).replace(".txt", ".json")

        FileManager.write_json(
            filename,
            screenplay_dict
        )

        return screenplay, filename