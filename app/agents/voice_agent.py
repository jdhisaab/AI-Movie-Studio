import os

from app.agents.base_agent import BaseAgent
from app.services.voice_service import VoiceService


class VoiceAgent(BaseAgent):
    """
    Generates voice audio for every narration scene.
    """

    def __init__(self):
        super().__init__()

        self.voice_service = VoiceService()

    def generate_voice(
        self,
        narrations,
        language="en"
    ):

        os.makedirs(
            "output/audio",
            exist_ok=True
        )

        audio_files = []

        for narration in narrations:

            print(
                f"🎙 Generating Voice for Scene {narration.scene_number}..."
            )

            output_file = (
                f"output/audio/scene_{narration.scene_number:03}.mp3"
            )

            self.voice_service.generate(
                text=narration.narration,
                language=language,
                output_file=output_file
            )

            audio_files.append(output_file)

            print(
                f"✅ Scene {narration.scene_number} Voice Generated"
            )

        return audio_files