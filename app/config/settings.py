from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Global application configuration.
    Change values here instead of hardcoding them
    throughout the project.
    """

    # =====================================================
    # Application
    # =====================================================

    APP_NAME: str = "AI Movie Studio"

    VERSION: str = "0.4.0"

    DEBUG: bool = True

    # =====================================================
    # Ollama
    # =====================================================

    OLLAMA_MODEL: str = "gemma4:e2b-it-qat"

    OLLAMA_HOST: str = "http://localhost:11434"

    OLLAMA_TEMPERATURE: float = 0.3

    OLLAMA_TOP_P: float = 0.9

    OLLAMA_NUM_CTX: int = 8192

    OLLAMA_NUM_PREDICT: int = 4096

    # =====================================================
    # Output Directories
    # =====================================================

    OUTPUT_DIR: str = "output"

    STORY_DIR: str = "output/stories"

    SCREENPLAY_DIR: str = "output/screenplays"

    SCENE_PLAN_DIR: str = "output/scene_plans"

    IMAGE_DIR: str = "output/images"

    AUDIO_DIR: str = "output/audio"

    VIDEO_DIR: str = "output/videos"

    # =====================================================
    # Image Settings
    # =====================================================

    IMAGE_PROVIDER: str = "local"

    IMAGE_WIDTH: int = 1280

    IMAGE_HEIGHT: int = 720

    IMAGE_FORMAT: str = "PNG"

    # =====================================================
    # Voice Settings
    # =====================================================

    VOICE_PROVIDER: str = "gtts"

    VOICE_LANGUAGE: str = "en"

    # =====================================================
    # Video Settings
    # =====================================================

    VIDEO_FPS: int = 24

    VIDEO_CODEC: str = "libx264"

    VIDEO_FORMAT: str = "mp4"

    # =====================================================
    # Logging
    # =====================================================

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "logs/movie_studio.log"