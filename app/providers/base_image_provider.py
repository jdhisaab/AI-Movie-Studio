from abc import ABC, abstractmethod


class BaseImageProvider(ABC):
    """
    Base interface for all image generation providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_file: str
    ) -> str:
        """
        Generate an image from a text prompt.

        Args:
            prompt: Image generation prompt.
            output_file: Path to save the generated image.

        Returns:
            Path of the generated image.
        """
        pass