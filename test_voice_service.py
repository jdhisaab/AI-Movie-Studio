from app.services.voice_service import VoiceService

service = VoiceService()

audio = service.generate(
    text="This is generated through Voice Service.",
    language="en",
    output_file="output/audio/service_test.mp3"
)

print(audio)