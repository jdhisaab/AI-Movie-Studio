from app.workflows.base_workflow import BaseWorkflow

from app.agents.image_prompt_agent import ImagePromptAgent
from app.agents.image_agent import ImageAgent


class ImageWorkflow(BaseWorkflow):

    def __init__(self):
        super().__init__()

        self.prompt_agent = ImagePromptAgent()
        self.image_agent = ImageAgent()

    def generate_images(self, screenplay):

        self.log_step("Generating Image Prompts")

        prompts = []

        for scene in screenplay.scenes:

            prompt = self.prompt_agent.generate_prompt(
                scene
            )

            prompts.append(prompt)

            self.log_success(
                f"Prompt Generated for Scene {scene.scene_number}"
            )

        self.log_step("Generating Images")

        image_files = self.image_agent.generate_images(
            prompts
        )

        self.log_success(
            f"{len(image_files)} Images Generated"
        )

        return image_files