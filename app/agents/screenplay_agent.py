from app.agents.base_agent import BaseAgent
from app.services.scene_mapper import SceneMapper
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class ScreenplayAgent(BaseAgent):
    """
    Generates screenplay from story.
    """

    def __init__(self):
        super().__init__()

    def generate_screenplay(
        self,
        story: str
    ):

        self.info("Generating Screenplay...")

        prompt = self.load_prompt(
            "screenplay_prompt.txt"
        )

        prompt = self.replace_variables(
            prompt,
            {
                "story": story
            }
        )

        response = self.generate(prompt)

        screenplay_dict = JsonParser.parse(
            response
        )

        screenplay = SceneMapper.from_dict(
            screenplay_dict
        )

        filename = FileManager.generate_filename(
            "screenplays",
            "screenplay"
        ).replace(
            ".txt",
            ".json"
        )

        FileManager.write_json(
            filename,
            screenplay_dict
        )

        self.success("Screenplay Generated")

        return screenplay, filename