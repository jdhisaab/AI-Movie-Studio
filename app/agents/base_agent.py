from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager
from app.utils.json_parser import JsonParser


class BaseAgent:
    """
    Base class for all AI agents.
    """

    def __init__(self):
        self.ollama = OllamaService()

    # ==================================================
    # Prompt Utilities
    # ==================================================

    def load_prompt(self, filename: str) -> str:
        """
        Load a prompt template from the prompts directory.
        """
        return FileManager.load_prompt(filename)

    def replace_variables(
        self,
        prompt: str,
        variables: dict
    ) -> str:
        """
        Replace variables inside prompt templates.

        Supports both:
            {variable}
            {{variable}}
        """

        for key, value in variables.items():

            # Replace {variable}
            prompt = prompt.replace(
                f"{{{key}}}",
                str(value)
            )

            # Replace {{variable}}
            prompt = prompt.replace(
                f"{{{{{key}}}}}",
                str(value)
            )

        return prompt

    # ==================================================
    # LLM Utilities
    # ==================================================

    def generate(
        self,
        prompt: str,
        temperature: float | None = None
    ) -> str:
        """
        Generate a text response using Ollama.
        """

        return self.ollama.generate(
            prompt=prompt,
            temperature=temperature
        )

    def generate_json(
        self,
        prompt: str,
        temperature: float | None = None
    ):
        """
        Generate and parse JSON response.
        """

        response = self.generate(
            prompt,
            temperature
        )

        return JsonParser.parse(response)

    # ==================================================
    # File Utilities
    # ==================================================

    def save_text(
        self,
        filename: str,
        content: str
    ):
        FileManager.write_text(
            filename,
            content
        )

    def save_json(
        self,
        filename: str,
        data
    ):
        FileManager.write_json(
            filename,
            data
        )

    def save_response(
        self,
        filename: str,
        content: str
    ):
        """
        Backward compatibility.
        """
        self.save_text(
            filename,
            content
        )

    def read_json(
        self,
        filename: str
    ):
        return FileManager.read_json(
            filename
        )

    # ==================================================
    # Logging Helpers
    # ==================================================

    def info(self, message: str):
        print(f"[INFO] {message}")

    def success(self, message: str):
        print(f"[SUCCESS] {message}")

    def warning(self, message: str):
        print(f"[WARNING] {message}")

    def error(self, message: str):
        print(f"[ERROR] {message}")