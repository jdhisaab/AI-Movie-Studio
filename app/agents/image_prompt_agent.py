from app.agents.base_agent import BaseAgent


class ImagePromptAgent(BaseAgent):
    """
    Generates an image prompt for each screenplay scene.
    """

    def __init__(self):
        super().__init__()

    def generate_prompt(self, scene):

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

        image_prompt = self.generate(prompt)

        self.success(
            f"Image Prompt Generated for Scene {scene.scene_number}"
        )

        return image_prompt.strip()