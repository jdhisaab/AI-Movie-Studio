from app.agents.story_agent import StoryAgent

print("=" * 50)
print("🎬 AI Movie Studio")
print("=" * 50)

story_agent = StoryAgent()

story_file = story_agent.generate_story(
    genre="Romance",
    language="English",
    duration=10
)

print("\n✅ Story Generated Successfully!")
print(f"\n📁 Saved to:\n{story_file}")