from app.models.narration import Narration


class NarrationMapper:

    @staticmethod
    def from_dict(data):

        narrations = []

        for item in data.get("narrations", []):

            narration = Narration(
                scene_number=item.get("scene_number", 0),
                narration=item.get("narration", "")
            )

            narrations.append(narration)

        return narrations