from app.config import settings

from app.providers.local_image_provider import LocalImageProvider
from app.providers.huggingface_provider import HuggingFaceProvider


class ImageService:
    """
    Service responsible for image generation.

    Selects the image provider based on the application settings.
    """

    def __init__(self):

        provider = settings.IMAGE_PROVIDER.lower()

        if provider == "huggingface":

            print("🖼️ Using Hugging Face Image Provider")

            self.provider = HuggingFaceProvider()

        else:

            print("🖼️ Using Local Image Provider")

            self.provider = LocalImageProvider()

    def generate(
        self,
        prompt: str,
        output_file: str
    ) -> str:

        return self.provider.generate(
            prompt=prompt,
            output_file=output_file
        )