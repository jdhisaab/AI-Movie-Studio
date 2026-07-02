from app.models.character import Character


class CharacterMapper:

    @staticmethod
    def from_dict(data):

        characters = []

        for item in data.get("characters", []):

            character = Character(
                name=item.get("name", ""),
                gender=item.get("gender", ""),
                age=item.get("age", ""),
                appearance=item.get("appearance", ""),
                personality=item.get("personality", ""),
                clothing=item.get("clothing", "")
            )

            characters.append(character)

        return characters