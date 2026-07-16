from app.agents.base_agent import BaseAgent


class StoryAgent(BaseAgent):
    """
    Generates the movie story.
    """

    def __init__(self):
        super().__init__()

    def generate_story(
        self,
        genre: str,
        language: str,
        duration: int
    ) -> str:

        self.info("Generating Story...")

        prompt = self.load_prompt(
            "story_prompt.txt"
        )

        prompt = self.replace_variables(
            prompt,
            {
                "genre": genre,
                "language": language,
                "duration": duration
            }
        )

        story = self.generate(prompt)

        self.success("Story Generated")

        return story