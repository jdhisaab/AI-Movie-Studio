from ollama import Client

from app.config.settings import settings


class OllamaService:
    """Service to communicate with the local Ollama server."""

    def __init__(self):
        self.client = Client(host=settings.OLLAMA_HOST)
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str) -> str:
        """Generate text using the configured Ollama model."""

        response = self.client.generate(
            model=self.model,
            prompt=prompt
        )

        return response["response"]