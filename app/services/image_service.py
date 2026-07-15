from app.providers.local_image_provider import LocalImageProvider


class ImageService:
    """
    Service responsible for image generation.
    """

    def __init__(self):

        self.provider = LocalImageProvider()

    def generate(
        self,
        prompt: str,
        output_file: str
    ):

        return self.provider.generate(
            prompt,
            output_file
        )