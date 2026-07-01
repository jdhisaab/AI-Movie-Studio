import os
import json
from datetime import datetime
from pathlib import Path
from datetime import datetime


class FileManager:
    """Handles reading and writing files."""

    @staticmethod
    def read_text(file_path: str) -> str:
        """Read text from a file."""
        return Path(file_path).read_text(encoding="utf-8")

    @staticmethod
    def write_text(file_path: str, content: str):
        """Write text to a file."""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    @staticmethod
    def generate_story_filename() -> str:
        """Generate a unique filename for a story."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"output/stories/story_{timestamp}.txt"

    @staticmethod
    def generate_filename(folder: str, prefix: str) -> str:
        """Generate a unique filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"output/{folder}/{prefix}_{timestamp}.txt"

    @staticmethod
    def write_json(file_path: str, data: dict):
        """Write dictionary to JSON file."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    @staticmethod
    def read_json(file_path: str):
        """Read JSON file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)