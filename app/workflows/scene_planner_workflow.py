import json
import os

from app.agents.scene_planner_agent import ScenePlannerAgent


class ScenePlannerWorkflow:

    def __init__(self):
        self.agent = ScenePlannerAgent()

    def generate_scene_plans(self, screenplay):

        print("\n🎬 Generating Scene Plans...\n")

        plans = []

        for scene in screenplay.scenes:

            plan = self.agent.generate_scene_plan(scene)

            plans.append(plan)

            print(f"✅ Scene {scene.scene_number} Planned")

        # -------------------------
        # Save Scene Plans
        # -------------------------

        os.makedirs("output/scene_plans", exist_ok=True)

        filename = "output/scene_plans/scene_plans.json"

        data = {
            "title": screenplay.title,
            "scene_plans": [
                plan.model_dump()
                for plan in plans
            ]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("\n✅ Scene Plans Saved:")
        print(filename)

        return plans