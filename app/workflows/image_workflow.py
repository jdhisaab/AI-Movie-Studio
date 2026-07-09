from app.agents.image_prompt_agent import ImagePromptAgent
from app.services.dummy_image_service import DummyImageService


class ImageWorkflow:

    def __init__(self):
        self.prompt_agent = ImagePromptAgent()
        self.image_service = DummyImageService()

    def generate_images(self, screenplay):

        generated_images = []

        print("\n🖼 Generating Images...\n")

        for scene in screenplay.scenes:

            prompt = self.prompt_agent.generate_prompt(scene)

            image = self.image_service.generate(
                scene.scene_number,
                scene.title
            )

            generated_images.append(image)

            print(f"✅ Scene {scene.scene_number} completed")

        return generated_images