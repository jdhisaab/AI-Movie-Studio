import ollama

from app.config import settings


class OllamaService:
    """
    Wrapper around the Ollama API.

    Every AI Agent in the project uses this service.
    """

    def __init__(self):
        self.model = settings.OLLAMA_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float | None = None
    ) -> str:
        """
        Generate a response from the configured Ollama model.
        """

        if temperature is None:
            temperature = settings.OLLAMA_TEMPERATURE

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                options={
                    "temperature": temperature,
                    "top_p": settings.OLLAMA_TOP_P,
                    "num_ctx": settings.OLLAMA_NUM_CTX,
                    "num_predict": settings.OLLAMA_NUM_PREDICT,
                },
            )

            return response["message"]["content"].strip()

        except Exception as ex:

            raise RuntimeError(
                f"Ollama generation failed: {ex}"
            ) from ex