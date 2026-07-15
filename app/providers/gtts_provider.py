import os

from gtts import gTTS

from app.providers.voice_provider import VoiceProvider


class GTTSProvider(VoiceProvider):

    def generate(
        self,
        text: str,
        language: str,
        output_file: str
    ):

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.save(output_file)

        return output_file