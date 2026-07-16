from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JsonParser


class ImagePromptAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_prompt(
        self,
        scene
    ):

        self.info(
            f"Generating Image Prompt for Scene {scene.scene_number}"
        )

        prompt = self.load_prompt(
            "image_prompt.txt"
        )

        prompt = self.replace_variables(
            prompt,
            {
                "scene": scene
            }
        )

        response = self.generate(prompt)

        data = JsonParser.parse(response)

        self.success(
            f"Image Prompt Generated for Scene {scene.scene_number}"
        )

        return data