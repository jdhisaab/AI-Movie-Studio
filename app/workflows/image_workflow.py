from app.workflows.base_workflow import BaseWorkflow

from app.agents.image_prompt_agent import ImagePromptAgent
from app.services.dummy_image_service import DummyImageService


class ImageWorkflow(BaseWorkflow):

    def __init__(self):
        super().__init__()

        self.prompt_agent = ImagePromptAgent()
        self.image_service = DummyImageService()

    def generate_images(self, screenplay):

        self.log_step("Generating Images")

        generated_images = []

        for scene in screenplay.scenes:

            prompt = self.prompt_agent.generate_prompt(scene)

            image = self.image_service.generate(
                scene.scene_number,
                scene.title
            )

            generated_images.append(image)

            self.log_success(
                f"Scene {scene.scene_number} completed"
            )

        return generated_images