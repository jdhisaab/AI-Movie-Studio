from app.agents.base_agent import BaseAgent
from app.services.narration_mapper import NarrationMapper


class NarrationAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_narration(self, screenplay):

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Title: {scene.title}

Narration: {scene.narration}

Actions: {scene.actions}

"""

        data = self.generate_json(
            "narration_prompt.txt",
            {
                "screenplay": screenplay_text
            }
        )

        narrations = NarrationMapper.from_dict(data)

        return narrations