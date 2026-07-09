import json


class JsonParser:
    """Utility class for parsing JSON responses from LLMs."""

    @staticmethod
    def parse(text: str):

        if not text:
            raise ValueError("Empty response from LLM")

        text = text.strip()

        # Remove Markdown code fences
        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        # Extract only the JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found in LLM response.")

        text = text[start:end + 1]

        try:
            return json.loads(text)

        except json.JSONDecodeError as e:

            print("\n" + "=" * 70)
            print("❌ JSON PARSE ERROR")
            print("=" * 70)
            print(f"Line      : {e.lineno}")
            print(f"Column    : {e.colno}")
            print(f"Message   : {e.msg}")
            print("=" * 70)

            lines = text.splitlines()

            start_line = max(0, e.lineno - 3)
            end_line = min(len(lines), e.lineno + 2)

            print("\nNearby JSON:\n")

            for i in range(start_line, end_line):
                prefix = ">>" if (i + 1) == e.lineno else "  "
                print(f"{prefix} {i+1}: {lines[i]}")

            print("\n" + "=" * 70)

            raise