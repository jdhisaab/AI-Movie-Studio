from app.agents.base_agent import BaseAgent
from app.services.image_service import ImageService


class ImageAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_images(self, prompts):

        image_files = []

        for index, prompt in enumerate(prompts, start=1):

            print(f"🖼 Generating Image {index}...")

            filename = f"output/images/scene_{index:03}.txt"

            image = ImageService.generate(
                prompt,
                filename
            )

            image_files.append(image)

        return image_files