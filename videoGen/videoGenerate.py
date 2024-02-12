from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def cut_video(input_video, output_video, timestamps):
    clips = []
    for segment in timestamps:
        start_time, end_time = segment['timestamp']
        clip = VideoFileClip(input_video).subclip(start_time , end_time)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_video)
    for clip in clips:
        clip.close()

# Example usage
if __name__=='main':
    input_video_path = 'F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Dramatic Final Over In FULL   Thrilling T20 Goes To Final Ball   England v New Zealand 2013.mp4'
    output_video_path = 'output_video.mp4'
    timestamps = [{'timestamp': [0.0, 9.0], 'text': " He's nailed this. He's high in the air. He's got enough. Oh, yes, he does. He's six."},{'timestamp': [20.0, 25.0], 'text': " picked it up the six pressure on Anderson. Ornith looks at it. That's good for a young gun."},{'timestamp': [33.0, 34.0], 'text': " And he's got not got this."},{'timestamp': [36.0, 38.0], 'text': ' Right, 19.1.'},{'timestamp': [39.0, 41.0], 'text': ' The 194 for three New Zealand.'},{'timestamp': [41.0, 43.0], 'text': ' 192 for five England.'},{'timestamp': [63.0, 65.0], 'text': " that's better. Dot ball. That ball for New Zealand went"},{'timestamp': [65.0, 66.0], 'text': ' for four.'},{'timestamp': [103.0, 105.0], 'text': " Tries the bounce and he's pulled into the leg side. He's got the crowd. Robbie Bupara has got the crowd. Fancy a nine. He's got the crowd."},{'timestamp': [133.46, 135.62], 'text': ' Down to a T20 here.'},{'timestamp': [185.0, 187.0], 'text': ' Like a side salad Cori Anderson. Good recovery is this.'},{'timestamp': [187.0, 189.0], 'text': ' Six off the first ball.'},{'timestamp': [205.88, 207.72], 'text': ' The final eight off two.'},{'timestamp': [208.44, 211.32], 'text': ' Left hand, though, hitting to the short boundary now.'},{'timestamp': [247.0, 250.0], 'text': ' Six for a super over.'},{'timestamp': [250.0, 252.0], 'text': ' And came super over.'},{'timestamp': [258.0, 260.0], 'text': ' Give it everything there Ben Stolkes'},{'timestamp': [322.52, 324.28], 'text': ' Robby with par a just a single'},{'timestamp': [324.28, 329.0], 'text': ' its New Zealand in a wonderfully entertaining game at T20 cricket.'},{'timestamp': [334.0, 336.0], 'text': ' Anderson, as did Butler.'},{'timestamp': [343.0, 345.36], 'text': ' Continuous changes of plans from Brendan McCullough,'}]

    cut_video(input_video_path, output_video_path, timestamps)
