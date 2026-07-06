from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


class DummyImageService:

    WIDTH = 1280
    HEIGHT = 720

    def generate(self, scene_number: int, scene_title: str):

        image = Image.new(
            "RGB",
            (self.WIDTH, self.HEIGHT),
            color=(30, 30, 30)
        )

        draw = ImageDraw.Draw(image)

        try:
            title_font = ImageFont.truetype("arial.ttf", 60)
            scene_font = ImageFont.truetype("arial.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            scene_font = ImageFont.load_default()

        draw.text(
            (60, 100),
            f"SCENE {scene_number:02}",
            fill="white",
            font=scene_font
        )

        draw.text(
            (60, 220),
            scene_title,
            fill="gold",
            font=title_font
        )

        draw.text(
            (60, 600),
            "AI Movie Studio",
            fill="lightgray",
            font=scene_font
        )

        output_dir = Path("output/images")
        output_dir.mkdir(parents=True, exist_ok=True)

        image_path = output_dir / f"scene_{scene_number:03}.png"

        image.save(image_path)

        return str(image_path)