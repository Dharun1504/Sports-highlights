from moviepy.editor import VideoFileClip

class Convertor:
    def to_wav(self, video_path, output_path):
        video_clip = VideoFileClip(video_path)

        audio_clip = video_clip.audio

        audio_clip.write_audiofile(output_path, codec='pcm_s16le', fps=44100)

        video_clip.close()
        audio_clip.close()


