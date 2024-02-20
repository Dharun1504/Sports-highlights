from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def modifyTS(a):
    t1 = a[0] - 2
    if(t1 < 0):
        t1 = 0
    return [t1, a[1] + 2]

def checkOverLap(a, b):
    if(a[1] > b[0]):
        b[0] = a[1]
    return b 

def check(timestamps):
    t = []
    for i in timestamps:
        if(len(t) != 0):
            t.append(checkOverLap(t[-1], modifyTS(i['timestamp'])))
        else:
            t.append(modifyTS(i['timestamp']))
    p = 0
    for i in timestamps:
        i["timestamp"] = t[p]
        p += 1
    return timestamps


def cut_video(input_video, output_video, timestamps):
    clips = []
    timestamps = check(timestamps)
    for segment in timestamps:
        start_time, end_time = segment['timestamp']
        clip = VideoFileClip(input_video).subclip(start_time , end_time)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_video)
    for clip in clips:
        clip.close()


# input_video_path = "F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Every Ball of the Extraordinary Final Over at Lord's!   England v Sri Lanka 2014.mp4"
# output_video_path = 'output_video_test.mp4'
# timestamps =[{'timestamp': (17.0, 20.0), 'text': " Max down the leg side and he's got it."}, {'timestamp': (26.0, 28.0), 'text': " It couldn't be tighter."}, {'timestamp': (28.0, 30.0), 'text': " It couldn't be more tense."}, {'timestamp': (35.0, 37.0), 'text': ' Another good catch from Matt Pryor.'}, {'timestamp': (44.0, 46.08), 'text': ' Really good catch from Matthew Price.'}, {'timestamp': (47.52, 48.84), 'text': ' Harath goes for one.'}, {'timestamp': (104.0, 109.12), 'text': ' Well, I reckon a more qualified right hand'}, {'timestamp': (112.72, 113.92), 'text': ' and around the off stump.'}, {'timestamp': (127.0, 133.0), 'text': " One pretty been behind it watched it didn't panic two balls remaining and need one wicked."}, {'timestamp': (144.0, 145.0), 'text': " That's the ball. That's the ball. That's the ball. That's the match. And that's the review."}, {'timestamp': (145.0, 147.0), 'text': " Well, I think he's inside edge this straight away."}, {'timestamp': (147.0, 148.0), 'text': " He's reviewed it."}, {'timestamp': (154.0, 156.0), 'text': " Oh, he's hit it."}, {'timestamp': (156.0, 172.0), 'text': " Oh, he's hit it. Oh, he's hit it. Which folks"}, {'timestamp': (172.0, 187.0), 'text': ' leaves us with one ball in the test match and one we It really is. Well, that is confirmation.'}, {'timestamp': (187.0, 188.0), 'text': " It's not out."}, {'timestamp': (194.0, 197.0), 'text': " It's come down to the very last ball."}, {'timestamp': (197.0, 204.0), 'text': " It's a good ball and it doesn't carry the slip."}, {'timestamp': (204.0, 208.0), 'text': ' And the match is drawn and the disbelief is apparent.'}]
# cut_video(input_video_path, output_video_path, timestamps)
