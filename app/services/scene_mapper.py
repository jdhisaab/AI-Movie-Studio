from app.models.scene import Scene
from app.models.screenplay import Screenplay


class SceneMapper:
    """Converts screenplay dictionary into Screenplay object."""

    @staticmethod
    def from_dict(data: dict) -> Screenplay:

        scenes = []

        for scene_data in data.get("scenes", []):
            # print(f"\nProcessing Scene {scene_data.get('scene_number')}")
            # print(scene_data)
            scene = Scene(
                scene_number=scene_data.get("scene_number", 0),
                title=scene_data.get("title", ""),
                narration=scene_data.get("narration", ""),
                characters=scene_data.get("characters", []),
                environment=scene_data.get("environment", ""),
                actions=scene_data.get("actions", ""),
                emotion=scene_data.get("emotion", ""),
                camera=scene_data.get("camera", "Wide Shot"),
                lighting=scene_data.get("lighting", "Natural Light"),
                duration=scene_data.get("duration", 8)
            )

            scenes.append(scene)

        return Screenplay(
            title=data.get("title", "Untitled Movie"),
            scenes=scenes
        )