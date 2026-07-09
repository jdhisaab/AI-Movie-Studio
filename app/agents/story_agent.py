from app.agents.base_agent import BaseAgent


class StoryAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def generate_story(self, genre, language, duration):

        prompt = self.load_prompt("story_prompt.txt")

        prompt = self.replace_variables(
            prompt,
            {
                "genre": genre,
                "language": language,
                "duration": duration
            }
        )

        story = self.generate(prompt)

        return story