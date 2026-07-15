from app.providers.gtts_provider import GTTSProvider

provider = GTTSProvider()

provider.generate(
    text="Welcome to AI Movie Studio.",
    language="en",
    output_file="output/audio/test.mp3"
)

print("Voice Generated Successfully")