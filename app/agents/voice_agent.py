import os

from app.agents.base_agent import BaseAgent
from app.config import settings
from app.services.voice_service import VoiceService


class VoiceAgent(BaseAgent):
    """
    Generates voice audio for narration scenes.
    """

    def __init__(self):
        super().__init__()

        self.voice_service = VoiceService()

    def generate_voice(
        self,
        narrations,
        language=None
    ):

        if language is None:
            language = settings.VOICE_LANGUAGE

        self.info("Generating Voice...")

        os.makedirs(
            settings.AUDIO_DIR,
            exist_ok=True
        )

        audio_files = []

        for narration in narrations:

            self.info(
                f"Generating Voice for Scene {narration.scene_number}"
            )

            output_file = os.path.join(
                settings.AUDIO_DIR,
                f"scene_{narration.scene_number:03}.mp3"
            )

            self.voice_service.generate(
                text=narration.narration,
                language=language,
                output_file=output_file
            )

            audio_files.append(
                output_file
            )

            self.success(
                f"Scene {narration.scene_number} Voice Generated"
            )

        self.success(
            f"{len(audio_files)} Voice Files Generated Successfully"
        )

        return audio_files