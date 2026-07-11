from app.agents.base_agent import BaseAgent


class ImagePromptAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_prompt(self, scene: str):

        data = self.generate_json(
            "image_prompt.txt",
            {
                "scene": scene
            }
        )

        return data