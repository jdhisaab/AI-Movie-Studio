from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.workflows.scene_planner_workflow import ScenePlannerWorkflow

story_agent = StoryAgent()
screenplay_agent = ScreenplayAgent()
workflow = ScenePlannerWorkflow()

story = story_agent.generate_story(
    genre="Romance",
    language="English",
    duration=10
)

screenplay, _ = screenplay_agent.generate_screenplay(story)

plans = workflow.generate_scene_plans(screenplay)



print("\n==============================")
print("🎬 Scene Planner Completed")
print("==============================")