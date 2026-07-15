import os

from app.agents.base_agent import BaseAgent
from app.services.image_service import ImageService


class ImageAgent(BaseAgent):

    def __init__(self):
        super().__init__()

        self.image_service = ImageService()

    def generate_images(
        self,
        prompts
    ):

        os.makedirs(
            "output/images",
            exist_ok=True
        )

        image_files = []

        for index, prompt in enumerate(
            prompts,
            start=1
        ):

            print(
                f"🖼 Generating Image {index}..."
            )

            output_file = (
                f"output/images/scene_{index:03}.png"
            )

            image = self.image_service.generate(
                prompt=prompt,
                output_file=output_file
            )

            image_files.append(image)

            print(
                f"✅ Scene {index} Image Generated"
            )

        return image_files