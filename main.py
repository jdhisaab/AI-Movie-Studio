from app.agents.story_agent import StoryAgent
from app.agents.screenplay_agent import ScreenplayAgent
from app.utils.file_manager import FileManager
from app.agents.image_prompt_agent import ImagePromptAgent
from app.agents.image_agent import ImageAgent
from app.agents.character_agent import CharacterAgent
from app.agents.narration_agent import NarrationAgent
def main():

    print("=" * 50)
    print("🎬 AI Movie Studio")
    print("=" * 50)

    # Generate Story
    story_agent = StoryAgent()

    story_file = story_agent.generate_story(
        genre="Romance",
        language="English",
        duration=1 #minutes
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
    image_prompt_agent = ImagePromptAgent()
    image_prompts = image_prompt_agent.generate_prompt(screenplay)
    print("\n========== IMAGE PROMPTS ==========\n")

    for i, prompt in enumerate(image_prompts, start=1):

        print(f"\nScene {i}\n")

        # print(prompt)

        print("-" * 80)
    
    image_agent = ImageAgent()
    image_files = image_agent.generate_images(image_prompts)
    print("\nGenerated Images:")

    for image in image_files:
        print(image)

    character_agent = CharacterAgent()
    characters = character_agent.generate_characters(screenplay)
    print("\n========== CHARACTERS ==========\n")

    for character in characters:

        print(f"Name: {character.name}")
        print(f"Gender: {character.gender}")
        print(f"Age: {character.age}")
        print(f"Appearance: {character.appearance}")
        print(f"Personality: {character.personality}")
        print(f"Clothing: {character.clothing}")
        print("-" * 50)


    narration_agent = NarrationAgent()
    narrations = narration_agent.generate_narration(screenplay)
    print("\n========== NARRATIONS ==========\n")

    for narration in narrations:

        print(f"Scene {narration.scene_number}")
        print(narration.narration)
        print("-" * 60)

if __name__ == "__main__":
    main()