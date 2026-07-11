import json
from dataclasses import asdict

from app.agents.base_agent import BaseAgent
from app.models.scene_plan import ScenePlan


class ScenePlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_scene_plan(self, scene):

        print(f"🎬 Planning Scene {scene.scene_number}...")

        scene_json = json.dumps(
            asdict(scene),
            indent=2
        )

        data = self.generate_json(
            "scene_planner_prompt.txt",
            {
                "scene": scene_json
            }
        )

        # -------------------------------------------------
        # Normalization
        # -------------------------------------------------

        data["scene_number"] = data.get(
            "scene_number",
            scene.scene_number
        )

        data["location"] = str(
            data.get("location", "Unknown")
        )

        data["time_of_day"] = str(
            data.get("time_of_day", "Day")
        )

        data["camera_motion"] = str(
            data.get("camera_motion", "Static")
        )

        data["character_motion"] = str(
            data.get("character_motion", "Idle")
        )

        data["background_motion"] = str(
            data.get("background_motion", "None")
        )

        data["style"] = str(
            data.get("style", "Hollywood Cinematic")
        )

        data["aspect_ratio"] = str(
            data.get("aspect_ratio", "16:9")
        )

        effects = data.get(
            "visual_effects",
            []
        )

        normalized = []

        if isinstance(effects, list):

            for effect in effects:

                if isinstance(effect, str):
                    normalized.append(effect)

                elif isinstance(effect, dict):

                    normalized.append(
                        effect.get(
                            "type",
                            effect.get(
                                "name",
                                effect.get(
                                    "effect",
                                    effect.get(
                                        "description",
                                        str(effect)
                                    )
                                )
                            )
                        )
                    )

                else:
                    normalized.append(str(effect))

        else:
            normalized = [str(effects)]

        data["visual_effects"] = normalized

        return ScenePlan(**data)