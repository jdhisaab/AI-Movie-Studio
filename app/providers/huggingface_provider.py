import os
import requests

from app.providers.base_image_provider import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):
    """
    Hugging Face Image Generation Provider.
    """

    def __init__(self):

        self.api_key = os.getenv("HF_API_KEY")

        self.model = (
            "black-forest-labs/FLUX.1-schnell"
        )

        self.api_url = (
            f"https://api-inference.huggingface.co/models/{self.model}"
        )

    def generate(
        self,
        prompt: str,
        output_file: str
    ) -> str:

        if not self.api_key:
            raise ValueError(
                "HF_API_KEY environment variable not found."
            )

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "inputs": prompt
        }

        print("\n🎨 Generating Image from Hugging Face...")
        print(f"Model : {self.model}")

        response = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=300
        )

        if response.status_code != 200:

            raise RuntimeError(
                f"HuggingFace Error ({response.status_code})\n"
                f"{response.text}"
            )

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        with open(output_file, "wb") as f:
            f.write(response.content)

        print(f"✅ Image Saved : {output_file}")

        return output_file