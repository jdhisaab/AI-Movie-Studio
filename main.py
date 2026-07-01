from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.utils.file_manager import FileManager


def main():

    print("=" * 50)
    print("🎬 AI Movie Studio")
    print("=" * 50)

    # Generate Story
    story_agent = StoryAgent()

    story_file = story_agent.generate_story(
        genre="Romance",
        language="English",
        duration=10
    )

    print(f"\n✅ Story Saved:\n{story_file}")

    # Read Story
    story = FileManager.read_text(story_file)

    # Generate Screenplay
    screenplay_agent = ScreenplayAgent()

    screenplay, screenplay_file = screenplay_agent.generate_screenplay(story)

    print("\nMovie Title:")
    print(screenplay.title)

    print("\nTotal Scenes:")
    print(len(screenplay.scenes))

    scene = screenplay.scenes[0]

    print("\nFirst Scene")
    print("Title:", scene.title)
    print("Camera:", scene.camera)
    print("Lighting:", scene.lighting)
    print("Emotion:", scene.emotion)

    print(f"\n✅ Screenplay Saved:\n{screenplay_file}")


if __name__ == "__main__":
    main()