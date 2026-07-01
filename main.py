from app.agents.story_agent import StoryAgent
from app.models.content_request import ContentRequest


def main():
    print("=" * 50)
    print("🎬 AI Movie Studio")
    print("=" * 50)

    request = ContentRequest(
        genre="Romance",
        language="English",
        duration=10,
        platform="YouTube",
        style="Cinematic"
    )

    story_agent = StoryAgent()

    story_file = story_agent.generate_story(
        genre=request.genre,
        language=request.language,
        duration=request.duration
    )

    print("\n✅ Story Generated Successfully!")
    print(f"\n📁 Story Saved:\n{story_file}")


if __name__ == "__main__":
    main()