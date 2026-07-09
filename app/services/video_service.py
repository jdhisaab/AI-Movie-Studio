import os
import subprocess


class VideoService:

    def create_video(
        self,
        image_folder="output/images",
        output_file="output/videos/movie.mp4",
        fps=1
    ):

        os.makedirs("output/videos", exist_ok=True)

        command = [
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", f"{image_folder}/scene_%03d.png",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            output_file
        ]

        print("\n🎬 Creating Video...\n")

        subprocess.run(command, check=True)

        print(f"\n✅ Video Saved:\n{output_file}")

        return output_file