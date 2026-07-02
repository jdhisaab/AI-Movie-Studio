import os


class ImageService:

    @staticmethod
    def generate(prompt: str, filename: str):

        os.makedirs("output/images", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(prompt)

        return filename