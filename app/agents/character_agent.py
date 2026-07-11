from app.agents.base_agent import BaseAgent
from app.services.character_mapper import CharacterMapper
from app.utils.json_parser import JsonParser


class CharacterAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_characters(self, screenplay):

        screenplay_text = ""

        for scene in screenplay.scenes:

            screenplay_text += f"""
Scene {scene.scene_number}

Characters: {", ".join(scene.characters)}

Narration: {scene.narration}

Actions: {scene.actions}

"""

        prompt = self.build_prompt(
            "character_prompt.txt",
            {
                "screenplay": screenplay_text
            }
        )

        response = self.generate(prompt)

        print("\n================ CHARACTER RESPONSE ================\n")
        print(response)
        print("\n====================================================\n")

        try:
            data = JsonParser.parse(response)

        except Exception as e:

            print("\n❌ Invalid JSON returned by Character Agent\n")

            raise e

        characters = CharacterMapper.from_dict(data)

        return characters