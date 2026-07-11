import json
import re


class JsonParser:
    """Utility class for parsing JSON responses from LLMs."""

    @staticmethod
    def parse(text: str):

        text = text.strip()

        # Remove markdown code fences
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # Extract the first complete JSON object
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            raise ValueError("No JSON object found in response.")

        json_text = match.group(0)

        return json.loads(json_text)