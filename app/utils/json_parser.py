import json


class JsonParser:
    """
    Robust JSON parser for LLM responses.

    Handles:
    - Markdown code fences
    - Extra explanations before/after JSON
    - Multiple JSON objects
    """

    @staticmethod
    def parse(text: str):

        text = text.strip()

        # Remove markdown fences
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        decoder = json.JSONDecoder()

        for i, ch in enumerate(text):

            if ch == "{":

                try:

                    obj, end = decoder.raw_decode(text[i:])

                    return obj

                except json.JSONDecodeError:
                    continue

        raise ValueError("No valid JSON object found.")