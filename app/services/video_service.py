import os
import subprocess

from moviepy import AudioFileClip, ImageClip

from app.config import settings


class VideoService:
    """
    Creates narrated scene videos using MoviePy
    and merges them using FFmpeg.
    """

    def __init__(self):

        os.makedirs(settings.VIDEO_DIR, exist_ok=True)

    def create_video(
        self,
        image_files,
        audio_files,
        output_file=None
    ):

        if output_file is None:
            output_file = os.path.join(
                settings.VIDEO_DIR,
                "movie.mp4"
            )

        temp_dir = os.path.join(
            settings.VIDEO_DIR,
            "temp"
        )

        os.makedirs(temp_dir, exist_ok=True)

        scene_videos = []

        print("\n🎬 Creating Scene Videos...\n")

        for index, (image, audio) in enumerate(
            zip(image_files, audio_files),
            start=1
        ):

            print(f"Creating Scene {index}")

            audio_clip = AudioFileClip(audio)

            clip = (
                ImageClip(image)
                .with_duration(audio_clip.duration)
                .with_audio(audio_clip)
            )

            scene_video = os.path.join(
                temp_dir,
                f"scene_{index:03}.mp4"
            )

            clip.write_videofile(
                scene_video,
                fps=settings.VIDEO_FPS,
                codec="libx264",
                audio_codec="aac",
                logger=None
            )

            clip.close()
            audio_clip.close()

            scene_videos.append(scene_video)

        list_file = os.path.join(
            temp_dir,
            "videos.txt"
        )

        with open(
            list_file,
            "w",
            encoding="utf-8"
        ) as f:

            for video in scene_videos:
                f.write(f"file '{os.path.abspath(video)}'\n")

        print("\n🎬 Merging Scene Videos...\n")

        command = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            list_file,
            "-c",
            "copy",
            output_file
        ]

        subprocess.run(
            command,
            check=True
        )

        print("\n✅ Movie Created Successfully")

        print(output_file)

        return output_file