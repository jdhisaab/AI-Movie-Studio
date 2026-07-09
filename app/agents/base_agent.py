from abc import ABC

from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager


class BaseAgent(ABC):

    def __init__(self):
        self.ollama = OllamaService()

    def load_prompt(self, filename: str) -> str:
        return FileManager.load_prompt(filename)

    def generate(self, prompt: str) -> str:
        response = self.ollama.generate(prompt)
        return response.strip()

    def replace_variables(self, prompt: str, variables: dict) -> str:

        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))

        return prompt