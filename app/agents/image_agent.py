import os

from app.services.image_service import ImageService


class ImageAgent:

    def generate_images(self, prompts):

        image_files = []

        for index, prompt in enumerate(prompts, start=1):

            filename = f"output/images/scene_{index:03}.txt"

            image = ImageService.generate(prompt, filename)

            image_files.append(image)

        return image_files