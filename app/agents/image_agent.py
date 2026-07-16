import os

from app.agents.base_agent import BaseAgent
from app.config import settings
from app.services.image_service import ImageService


class ImageAgent(BaseAgent):
    """
    Generates images from image prompts.
    """

    def __init__(self):
        super().__init__()

        self.image_service = ImageService()

    def generate_images(self, prompts):

        self.info("Generating Images...")

        os.makedirs(
            settings.IMAGE_DIR,
            exist_ok=True
        )

        image_files = []

        for index, prompt in enumerate(
            prompts,
            start=1
        ):

            self.info(
                f"Generating Image {index}"
            )

            output_file = os.path.join(
                settings.IMAGE_DIR,
                f"scene_{index:03}.png"
            )

            image_path = self.image_service.generate(
                prompt=prompt,
                output_file=output_file
            )

            image_files.append(
                image_path
            )

            self.success(
                f"Scene {index} Image Generated"
            )

        self.success(
            f"{len(image_files)} Images Generated Successfully"
        )

        return image_files