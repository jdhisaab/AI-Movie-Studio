from app.services.dummy_image_service import DummyImageService

service = DummyImageService()

service.generate(
    1,
    "The Architect's Monolith"
)

print("Image Generated Successfully!")