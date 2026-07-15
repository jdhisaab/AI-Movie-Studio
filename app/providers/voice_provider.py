from abc import ABC, abstractmethod


class VoiceProvider(ABC):

    @abstractmethod
    def generate(
        self,
        text: str,
        language: str,
        output_file: str
    ):
        pass