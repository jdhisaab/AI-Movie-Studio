from app.providers.gtts_provider import GTTSProvider


class VoiceService:
    """
    Voice generation service.
    """

    def __init__(self):

        self.provider = GTTSProvider()

    def generate(
        self,
        text: str,
        language: str,
        output_file: str
    ):

        return self.provider.generate(
            text=text,
            language=language,
            output_file=output_file
        )