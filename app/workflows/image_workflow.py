import os

from app.workflows.base_workflow import BaseWorkflow

from app.agents.image_prompt_agent import ImagePromptAgent
from app.services.image_service import ImageService

from app.config import settings


class ImageWorkflow(BaseWorkflow):
    """
    Workflow responsible for generating images
    for every screenplay scene.
    """

    def __init__(self):

        super().__init__()

        self.prompt_agent = ImagePromptAgent()
        self.image_service = ImageService()

    def generate_images(self, screenplay):

        self.log_step("Generating Scene Images")

        os.makedirs(
            settings.IMAGE_DIR,
            exist_ok=True
        )

        generated_images = []

        for scene in screenplay.scenes:

            self.log_info(
                f"Generating prompt for Scene {scene.scene_number}"
            )

            prompt = self.prompt_agent.generate_prompt(scene)

            output_file = os.path.join(
                settings.IMAGE_DIR,
                f"scene_{scene.scene_number:03}.png"
            )

            image = self.image_service.generate(
                prompt=prompt,
                output_file=output_file
            )

            generated_images.append(image)

            self.log_success(
                f"Scene {scene.scene_number} image generated"
            )

        self.log_success(
            f"{len(generated_images)} Images Generated"
        )

        return generated_images