from app.workflows.base_workflow import BaseWorkflow

from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.agents.narration_agent import NarrationAgent
from app.agents.character_agent import CharacterAgent

from app.workflows.scene_planner_workflow import ScenePlannerWorkflow
from app.workflows.image_workflow import ImageWorkflow

from app.services.video_service import VideoService


class MovieWorkflow(BaseWorkflow):

    def __init__(self):

        super().__init__()

        self.story_agent = StoryAgent()
        self.screenplay_agent = ScreenplayAgent()
        self.narration_agent = NarrationAgent()
        self.character_agent = CharacterAgent()

        self.scene_planner_workflow = ScenePlannerWorkflow()
        self.image_workflow = ImageWorkflow()

        self.video_service = VideoService()

    def run(self, genre, language, duration):

        self.header("AI MOVIE STUDIO")

        # --------------------------------------------------
        # Story
        # --------------------------------------------------

        self.log_step("Generating Story")

        story_file = self.story_agent.generate_story(
            genre=genre,
            language=language,
            duration=duration
        )

        self.log_success("Story Generated")

        # --------------------------------------------------
        # Screenplay
        # --------------------------------------------------

        self.log_step("Generating Screenplay")

        screenplay, screenplay_file = \
            self.screenplay_agent.generate_screenplay(
                story_file
            )

        self.log_success("Screenplay Generated")

        # --------------------------------------------------
        # Narration
        # --------------------------------------------------

        self.log_step("Generating Narration")

        narrations = self.narration_agent.generate_narration(
            screenplay
        )

        self.log_success("Narration Generated")

        # --------------------------------------------------
        # Characters
        # --------------------------------------------------

        self.log_step("Generating Characters")

        characters = self.character_agent.generate_characters(
            screenplay
        )

        self.log_success("Characters Generated")

        # --------------------------------------------------
        # Scene Plans
        # --------------------------------------------------

        scene_plans = \
            self.scene_planner_workflow.generate_scene_plans(
                screenplay
            )

        # --------------------------------------------------
        # Images
        # --------------------------------------------------

        images = self.image_workflow.generate_images(
            screenplay
        )

        self.log_success("Images Generated")

        # --------------------------------------------------
        # Video
        # --------------------------------------------------

        self.log_step("Generating Video")

        video = self.video_service.create_video()

        self.log_success("Video Generated")

        self.footer("MOVIE WORKFLOW COMPLETED")

        return {
            "story_file": story_file,
            "screenplay_file": screenplay_file,
            "screenplay": screenplay,
            "characters": characters,
            "narrations": narrations,
            "scene_plans": scene_plans,
            "images": images,
            "video": video
        }