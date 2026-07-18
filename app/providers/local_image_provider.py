import os

from PIL import Image, ImageDraw, ImageFont

from app.config import settings
from app.providers.base_image_provider import BaseImageProvider


class LocalImageProvider(BaseImageProvider):
    """
    Local placeholder image provider.

    Generates a clean placeholder image for each scene.
    This provider is useful during development before
    integrating a real AI image generator.
    """

    def __init__(self):

        self.width = settings.IMAGE_WIDTH
        self.height = settings.IMAGE_HEIGHT

    def generate(
        self,
        prompt: str,
        output_file: str
    ) -> str:

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        image = Image.new(
            "RGB",
            (self.width, self.height),
            color=(25, 30, 40)
        )

        draw = ImageDraw.Draw(image)

        try:
            title_font = ImageFont.truetype(
                "arial.ttf",
                42
            )

            text_font = ImageFont.truetype(
                "arial.ttf",
                28
            )

        except Exception:

            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        title = "AI MOVIE STUDIO"

        title_bbox = draw.textbbox(
            (0, 0),
            title,
            font=title_font
        )

        title_width = title_bbox[2] - title_bbox[0]

        draw.text(
            (
                (self.width - title_width) / 2,
                80
            ),
            title,
            fill="white",
            font=title_font
        )

        # --------------------------------------------------
        # Placeholder
        # --------------------------------------------------

        placeholder = "Scene Placeholder"

        placeholder_bbox = draw.textbbox(
            (0, 0),
            placeholder,
            font=text_font
        )

        placeholder_width = (
            placeholder_bbox[2] -
            placeholder_bbox[0]
        )

        draw.text(
            (
                (self.width - placeholder_width) / 2,
                220
            ),
            placeholder,
            fill=(220, 220, 220),
            font=text_font
        )

        # --------------------------------------------------
        # Output File Name
        # --------------------------------------------------

        scene_name = os.path.basename(output_file)

        scene_bbox = draw.textbbox(
            (0, 0),
            scene_name,
            font=text_font
        )

        scene_width = scene_bbox[2] - scene_bbox[0]

        draw.text(
            (
                (self.width - scene_width) / 2,
                320
            ),
            scene_name,
            fill=(100, 220, 255),
            font=text_font
        )

        # --------------------------------------------------
        # Bottom Information
        # --------------------------------------------------

        footer = "Waiting for AI Image Generation"

        footer_bbox = draw.textbbox(
            (0, 0),
            footer,
            font=text_font
        )

        footer_width = footer_bbox[2] - footer_bbox[0]

        draw.text(
            (
                (self.width - footer_width) / 2,
                self.height - 100
            ),
            footer,
            fill=(180, 180, 180),
            font=text_font
        )

        image.save(output_file)

        print(f"🖼️ Placeholder Image Saved : {output_file}")

        return output_file