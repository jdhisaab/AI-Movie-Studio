from app.utils.file_manager import FileManager
from app.services.ollama_service import OllamaService


class ImagePromptAgent:

    def __init__(self):
        self.ollama = OllamaService()

    def generate_prompts(self, screenplay):

        prompt_template = FileManager.read_text(
            "app/prompts/image_prompt.txt"
        )

        prompts = []

        for scene in screenplay.scenes:

            scene_text = f"""
Title: {scene.title}

Narration: {scene.narration}

Characters: {', '.join(scene.characters)}

Environment: {scene.environment}

Actions: {scene.actions}

Emotion: {scene.emotion}

Camera: {scene.camera}

Lighting: {scene.lighting}
"""

            prompt = prompt_template.format(scene=scene_text)

            image_prompt = self.ollama.generate(prompt)

            prompts.append(image_prompt)

        return prompts