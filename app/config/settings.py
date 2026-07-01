from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Settings:
    """Application Settings"""

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST")

    LANGUAGE = os.getenv("LANGUAGE")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR")
    LOG_LEVEL = os.getenv("LOG_LEVEL")


settings = Settings()