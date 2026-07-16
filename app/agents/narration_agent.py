from app.agents.base_agent import BaseAgent
from app.services.narration_mapper import NarrationMapper
from app.utils.json_parser import JsonParser


class NarrationAgent(BaseAgent):
    """
    Generates narration for every screenplay scene.
    """

    def __init__(self):
        super().__init__()

    def generate_narration(self, screenplay):

        self.info("Generating Narration...")

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Title: {scene.title}

Narration: {scene.narration}

Actions: {scene.actions}

"""

        prompt = self.load_prompt(
            "narration_prompt.txt"
        )

        prompt = self.replace_variables(
            prompt,
            {
                "screenplay": screenplay_text
            }
        )

        response = self.generate(prompt)

        data = JsonParser.parse(response)

        narrations = NarrationMapper.from_dict(data)

        self.success("Narration Generated")

        return narrations