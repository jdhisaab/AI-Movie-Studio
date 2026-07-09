from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.agents.narration_agent import NarrationAgent
from app.agents.character_agent import CharacterAgent
from app.workflows.image_workflow import ImageWorkflow
from app.services.video_service import VideoService

class MovieWorkflow:

    def __init__(self):
        self.story_agent = StoryAgent()
        self.screenplay_agent = ScreenplayAgent()
        self.narration_agent = NarrationAgent()
        self.character_agent = CharacterAgent()
        self.image_workflow = ImageWorkflow()
        self.video_service = VideoService()
    def run(self, genre, language, duration):

        print("\n" + "=" * 60)
        print("🎬 AI MOVIE STUDIO")
        print("=" * 60)

        # -----------------------------------
        # Step 1 : Story
        # -----------------------------------

        print("\n📖 Generating Story...\n")

        story_file = self.story_agent.generate_story(
            genre=genre,
            language=language,
            duration=duration
        )

        print("✅ Story Generated")

        # -----------------------------------
        # Step 2 : Screenplay
        # -----------------------------------

        print("\n🎞 Generating Screenplay...\n")

        screenplay, screenplay_file = self.screenplay_agent.generate_screenplay(
            story_file
        )

        print("✅ Screenplay Generated")

        # -----------------------------------
        # Step 3 : Narration
        # -----------------------------------

        print("\n🎤 Generating Narration...\n")

        narrations = self.narration_agent.generate_narration(
            screenplay
        )

        print("✅ Narration Generated")

        # -----------------------------------
        # Step 4 : Characters
        # -----------------------------------

        print("\n👤 Generating Characters...\n")

        characters = self.character_agent.generate_characters(
            screenplay
        )

        print("✅ Characters Generated")

        # -----------------------------------
        # Step 5 : Images
        # -----------------------------------

        images = self.image_workflow.generate_images(
            screenplay
        )

        print("\n✅ Images Generated")

        # -----------------------------------
        # Step 6 : Video
        # -----------------------------------

        video = self.video_service.create_video()

        print("\n✅ Video Generated")

        
        print("\n" + "=" * 60)
        print("🎉 MOVIE WORKFLOW COMPLETED")
        print("=" * 60)


        

        return {
           "story_file": story_file,
            "screenplay_file": screenplay_file,
            "screenplay": screenplay,
            "narrations": narrations,
            "characters": characters,
            "images": images,
            "video": video
        }