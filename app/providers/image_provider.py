from abc import ABC, abstractmethod


class ImageProvider(ABC):
    """
    Base class for all image providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_file: str
    ) -> str:
        pass