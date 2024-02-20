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


input_video_path = 'F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Russell & Warner-ன் ஒரு தரமான Batting Show   #AUSvWI 3rd T20I Tamil Highlights.mp4'
output_video_path = 'output_video_tamil.mp4'
timestamps =[{"text": "Australia vs West Indies, 3-0-20 international", "timestamp": [0.0, 3.44]}, {"text": "Powerful batting line, we are able to do better in the 3rd match", "timestamp": [12.0, 16.4]}, {"text": "Out", "timestamp": [39.8, 45.0]}, {"text": "ou theyeri, easy catch", "timestamp": [45.0, 49.3]}, {"text": "Out", "timestamp": [54.5, 59.0]}, {"text": "1-star out.", "timestamp": [65.24, 70.52]}, {"text": "3-4-7.", "timestamp": [91.4, 96.52]}, {"text": "Super shot.", "timestamp": [99.88, 105.28]}, {"text": "What a shot.", "timestamp": [118.72, 124.52]}, {"text": "Goal.", "timestamp": [141.64, 147.84]}, {"text": "Out.", "timestamp": [168.52, 174.88]}, {"text": "A six shot!", "timestamp": [529.74, 535.94]}, {"text": "Go!", "timestamp": [667.88, 673.88]}, {"text": "Clean Maxwell gone.", "timestamp": [668.88, 674.88]}, {"text": "152 for 5.", "timestamp": [679.88, 685.88]}]
cut_video(input_video_path, output_video_path, timestamps)
