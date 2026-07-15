from app.workflows.base_workflow import BaseWorkflow
from app.agents.voice_agent import VoiceAgent


class VoiceWorkflow(BaseWorkflow):

    def __init__(self):
        super().__init__()

        self.voice_agent = VoiceAgent()

    def generate_voice(
        self,
        narrations,
        language="en"
    ):

        self.log_step("Generating Voice")

        audio_files = self.voice_agent.generate_voice(
            narrations=narrations,
            language=language
        )

        self.log_success(
            f"{len(audio_files)} Audio Files Generated"
        )

        return audio_files