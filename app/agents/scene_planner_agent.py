import json
from dataclasses import asdict

from app.models.scene_plan import ScenePlan
from app.services.ollama_service import OllamaService
from app.utils.file_manager import FileManager


class ScenePlannerAgent:

    def __init__(self):
        self.ollama = OllamaService()

    def generate_scene_plan(self, scene):

        print(f"🎬 Planning Scene {scene.scene_number}...")

        # Load prompt
        prompt = FileManager.load_prompt("scene_planner_prompt.txt")

        # Convert scene dataclass to JSON
        scene_json = json.dumps(
            asdict(scene),
            indent=2
        )

        prompt = prompt.replace("{scene}", scene_json)

        # Generate response
        response = self.ollama.generate(prompt)

        response = response.strip()

        # Remove markdown code blocks if present
        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:

            print("\n================ RAW RESPONSE ================\n")
            print(response)
            print("\n==============================================\n")

            raise e

        # ---------- Normalization ----------

        # Scene Number
        data["scene_number"] = data.get(
            "scene_number",
            scene.scene_number
        )

        # Strings
        data["location"] = str(data.get("location", "Unknown"))
        data["time_of_day"] = str(data.get("time_of_day", "Day"))
        data["camera_motion"] = str(data.get("camera_motion", "Static"))
        data["character_motion"] = str(data.get("character_motion", "Idle"))
        data["background_motion"] = str(data.get("background_motion", "None"))
        data["style"] = str(data.get("style", "Hollywood Cinematic"))
        data["aspect_ratio"] = str(data.get("aspect_ratio", "16:9"))

        # Normalize visual_effects
        effects = data.get("visual_effects", [])

        normalized_effects = []

        if isinstance(effects, list):

            for effect in effects:

                if isinstance(effect, str):
                    normalized_effects.append(effect)

                elif isinstance(effect, dict):

                    if "type" in effect:
                        normalized_effects.append(effect["type"])

                    elif "name" in effect:
                        normalized_effects.append(effect["name"])

                    elif "effect" in effect:
                        normalized_effects.append(effect["effect"])

                    elif "description" in effect:
                        normalized_effects.append(effect["description"])

                    else:
                        normalized_effects.append(str(effect))

                else:
                    normalized_effects.append(str(effect))

        else:
            normalized_effects = [str(effects)]

        data["visual_effects"] = normalized_effects

        # Create ScenePlan
        scene_plan = ScenePlan(**data)

        return scene_plan