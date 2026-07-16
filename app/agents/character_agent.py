from app.agents.base_agent import BaseAgent
from app.services.character_mapper import CharacterMapper
from app.utils.json_parser import JsonParser


class CharacterAgent(BaseAgent):
    """
    Generates movie characters from screenplay.
    """

    def __init__(self):
        super().__init__()

    def generate_characters(self, screenplay):

        self.info("Generating Characters...")

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Characters: {", ".join(scene.characters)}

Narration: {scene.narration}

Actions: {scene.actions}

"""

        prompt = self.load_prompt(
            "character_prompt.txt"
        )

        prompt = self.replace_variables(
            prompt,
            {
                "screenplay": screenplay_text
            }
        )

        response = self.generate(prompt)

        try:

            print("\n================ CHARACTER AI RESPONSE ================\n")
            print(response)
            print("\n=======================================================\n")

            data = JsonParser.parse(response)

        except Exception:

            print("\n========== RAW CHARACTER RESPONSE ==========\n")
            print(response)
            print("\n============================================\n")
            raise

        characters = CharacterMapper.from_dict(data)

        self.success("Characters Generated")

        return characters