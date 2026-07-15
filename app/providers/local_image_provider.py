import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from app.providers.image_provider import ImageProvider


class LocalImageProvider(ImageProvider):
    """
    Creates placeholder PNG images locally.
    Later this can be replaced with Fal.ai.
    """

    WIDTH = 1280
    HEIGHT = 720

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
            (self.WIDTH, self.HEIGHT),
            color=(30, 30, 30)
        )

        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(
                "arial.ttf",
                26
            )
        except Exception:
            font = ImageFont.load_default()

        wrapped = textwrap.fill(
            prompt,
            width=60
        )

        draw.multiline_text(
            (50, 50),
            wrapped,
            fill="white",
            font=font,
            spacing=8
        )

        image.save(output_file)

        return output_file