import json
import os

from app.workflows.base_workflow import BaseWorkflow
from app.agents.scene_planner_agent import ScenePlannerAgent


class ScenePlannerWorkflow(BaseWorkflow):

    def __init__(self):
        super().__init__()

        self.agent = ScenePlannerAgent()

    def generate_scene_plans(self, screenplay):

        self.log_step("Generating Scene Plans")

        plans = []

        for scene in screenplay.scenes:

            plan = self.agent.generate_scene_plan(scene)

            plans.append(plan)

            self.log_success(
                f"Scene {scene.scene_number} Planned"
            )

        os.makedirs(
            "output/scene_plans",
            exist_ok=True
        )

        filename = "output/scene_plans/scene_plans.json"

        data = {
            "title": screenplay.title,
            "scene_plans": [
                plan.model_dump()
                for plan in plans
            ]
        }

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

        self.log_success(
            f"Scene Plans Saved: {filename}"
        )

        return plans