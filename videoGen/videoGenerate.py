from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips


class GenerateVideo:

    def __init__(self):
        self.time = []
        self.count = 1
        self.transcribe = ''

    def getTimeStamp(self):
        for i in self.transcribe:
            self.time.append(i['timestamp'])

    def cut_video(self, input_file, output_file, start_time, end_time):
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

    def generateClips(self):
        input_file = 'video.mp4'
        for i in self.time:
            start_time = i[0] 
            end_time = i[1]
            output_file = f"clip{self.count}.mp4"
            self.count += 1 
            self.cut_video(input_file, output_file , start_time, end_time)

    def generateHighLightVideo(self,transcribe):
        self.transcribe = transcribe
        self.getTimeStamp()
        self.generateClips()
        clips = []
        for i in range(1,self.count):
            clip = VideoFileClip(f"clip{i}.mp4")
            clips.append(clip)
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile('highlights.mp4')

        


t = [{'text': ' What an over. It turned out to be a game', 'timestamp': [0.0, 3.0]}, {'text': " changing over. I'm concerned probably the", 'timestamp': [3.0, 6.0]}, {'text': ' world of the tournament so far for me.', 'timestamp': [6.0, 8.0]}, {'text': ' Absolutely brilliant. Just a single', 'timestamp': [8.0, 11.0]}, {'text': ' that was off a leg by from Mustafa Zur and', 'timestamp': [11.0, 14.0]}, {'text': ' five dots including a wicked.', 'timestamp': [14.0, 16.0]}, {'text': ' Incredible over. The big call.', 'timestamp': [16.0, 21.0]}, {'text': " A big decision for Bangladesh and they've", 'timestamp': [21.0, 23.0]}]

g = GenerateVideo()
g.generateHighLightVideo(transcribe=t)