from abc import ABC

from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    Handles:
    - Prompt loading
    - Variable replacement
    - LLM generation
    - JSON parsing
    """

    def __init__(self):
        self.ollama = OllamaService()

    # ---------------------------------------------------------
    # Prompt Utilities
    # ---------------------------------------------------------

    def load_prompt(self, filename: str) -> str:
        return FileManager.load_prompt(filename)

    def replace_variables(self, prompt: str, variables: dict) -> str:

        for key, value in variables.items():
            prompt = prompt.replace(
                f"{{{key}}}",
                str(value)
            )

        return prompt

    def build_prompt(
        self,
        prompt_file: str,
        variables: dict
    ) -> str:

        prompt = self.load_prompt(prompt_file)

        return self.replace_variables(
            prompt,
            variables
        )

    # ---------------------------------------------------------
    # LLM
    # ---------------------------------------------------------

    def generate(self, prompt: str) -> str:

        response = self.ollama.generate(prompt)

        return response.strip()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def clean_response(self, text: str) -> str:

        text = text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return text.strip()

    def generate_json(
        self,
        prompt_file: str,
        variables: dict
    ):

        prompt = self.build_prompt(
            prompt_file,
            variables
        )

        response = self.generate(prompt)

        response = self.clean_response(response)

        return JsonParser.parse(response)

    def generate_text(
        self,
        prompt_file: str,
        variables: dict
    ) -> str:

        prompt = self.build_prompt(
            prompt_file,
            variables
        )

        response = self.generate(prompt)

        return self.clean_response(response)