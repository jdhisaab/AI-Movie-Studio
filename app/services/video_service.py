import os

from moviepy import (
    AudioFileClip,
    ImageClip,
    concatenate_videoclips
)

from app.config import settings


class VideoService:
    """
    Creates a narrated movie from scene images and audio.
    """

    def create_video(
        self,
        image_files,
        audio_files,
        output_file=None
    ):

        if output_file is None:

            os.makedirs(
                settings.VIDEO_DIR,
                exist_ok=True
            )

            output_file = os.path.join(
                settings.VIDEO_DIR,
                "movie.mp4"
            )

        clips = []

        for image, audio in zip(
            image_files,
            audio_files
        ):

            audio_clip = AudioFileClip(audio)

            image_clip = (
                ImageClip(image)
                .with_duration(audio_clip.duration)
                .with_audio(audio_clip)
            )

            clips.append(image_clip)

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        final_video.write_videofile(
            output_file,
            fps=settings.VIDEO_FPS,
            codec="libx264",
            audio_codec="aac"
        )

        final_video.close()

        for clip in clips:
            clip.close()

        return output_file