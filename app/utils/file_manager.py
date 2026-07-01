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

    # @staticmethod
    # def generate_story_filename() -> str:
    #     """Generate a unique filename for a story."""
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     return f"output/stories/story_{timestamp}.txt"

    @staticmethod
    def generate_filename(folder: str, prefix: str) -> str:
        """Generate a unique filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"output/{folder}/{prefix}_{timestamp}.txt"