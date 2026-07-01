from app.services.ollama_service import OllamaService

print("🎬 AI Movie Studio")
print("=" * 40)

service = OllamaService()

response = service.generate(
    "Write a 100-word emotional story about true friendship."
)

print(response)