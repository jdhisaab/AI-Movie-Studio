from app.workflows.base_workflow import BaseWorkflow

from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.agents.character_agent import CharacterAgent
from app.agents.narration_agent import NarrationAgent

from app.workflows.scene_planner_workflow import ScenePlannerWorkflow
from app.workflows.image_workflow import ImageWorkflow
from app.workflows.voice_workflow import VoiceWorkflow

from app.services.video_service import VideoService

from app.config import settings


class MovieWorkflow(BaseWorkflow):
    """
    Main workflow responsible for generating
    the complete AI movie.
    """

    def __init__(self):

        super().__init__()

        # Agents
        self.story_agent = StoryAgent()
        self.screenplay_agent = ScreenplayAgent()
        self.character_agent = CharacterAgent()
        self.narration_agent = NarrationAgent()

        # Workflows
        self.scene_planner_workflow = ScenePlannerWorkflow()
        self.image_workflow = ImageWorkflow()
        self.voice_workflow = VoiceWorkflow()

        # Services
        self.video_service = VideoService()

    def run(
        self,
        genre: str,
        language: str,
        duration: int
    ):

        self.header("AI MOVIE STUDIO")

        # --------------------------------------------------------
        # Story
        # --------------------------------------------------------

        self.log_step("Generating Story")

        story = self.story_agent.generate_story(
            genre=genre,
            language=language,
            duration=duration
        )

        self.log_success("Story Generated")

        # --------------------------------------------------------
        # Screenplay
        # --------------------------------------------------------

        self.log_step("Generating Screenplay")

        screenplay, screenplay_file = (
            self.screenplay_agent.generate_screenplay(
                story
            )
        )

        self.log_success("Screenplay Generated")
        # --------------------------------------------------------
        # Developer Mode
        # --------------------------------------------------------

        if settings.DEV_MODE:

            original_scene_count = len(screenplay.scenes)

            screenplay.scenes = screenplay.scenes[
                :settings.DEV_MAX_SCENES
            ]

            self.log_info(
                f"Developer Mode: Reduced scenes "
                f"from {original_scene_count} "
                f"to {len(screenplay.scenes)}"
            )
        # --------------------------------------------------------
        # Characters
        # --------------------------------------------------------

        self.log_step("Generating Characters")

        characters = self.character_agent.generate_characters(
            screenplay
        )

        self.log_success("Characters Generated")

        # --------------------------------------------------------
        # Narration
        # --------------------------------------------------------

        self.log_step("Generating Narration")

        narrations = self.narration_agent.generate_narration(
            screenplay
        )

        self.log_success("Narration Generated")

        # --------------------------------------------------------
        # Voice
        # --------------------------------------------------------

        self.log_step("Generating Voice")

        audio_files = self.voice_workflow.generate_voice(
            narrations=narrations,
            language=settings.VOICE_LANGUAGE
        )

        self.log_success("Voice Generated")

        # --------------------------------------------------------
        # Scene Plans
        # --------------------------------------------------------

        self.log_step("Planning Scenes")

        scene_plans = (
            self.scene_planner_workflow.generate_scene_plans(
                screenplay
            )
        )

        self.log_success("Scene Plans Generated")

        # --------------------------------------------------------
        # Images
        # --------------------------------------------------------

        if settings.DEV_SKIP_IMAGE_GENERATION:

            self.log_warning(
                "Developer Mode: Skipping Image Generation"
            )

            images = []

        else:

            images = self.image_workflow.generate_images(
                screenplay
            )

            self.log_success("Images Generated")

        

        # --------------------------------------------------------
        # Video
        # --------------------------------------------------------

        if settings.DEV_SKIP_VIDEO_GENERATION:

            self.log_warning(
                "Developer Mode: Skipping Video Generation"
            )

            video = None

        else:

            self.log_step("Generating Video")

            video = self.video_service.create_video(
                image_files=images,
                audio_files=audio_files
            )

            self.log_success("Video Generated")

        self.footer("MOVIE WORKFLOW COMPLETED")

        return {
            "story": story,
            "screenplay": screenplay,
            "screenplay_file": screenplay_file,
            "characters": characters,
            "narrations": narrations,
            "scene_plans": scene_plans,
            "images": images,
            "voice_files": audio_files,
            "video": video,
        }