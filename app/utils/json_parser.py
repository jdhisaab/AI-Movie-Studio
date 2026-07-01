import json


class JsonParser:
    """Utility class for parsing JSON responses from LLMs."""

    @staticmethod
    def parse(text: str):
        """
        Parse JSON returned by the LLM.
        """

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)