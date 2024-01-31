from vidAud import Convertor


input_video_path = "F:\Cricket-data\Dramatic Final Over In FULL   Thrilling T20 Goes To Final Ball   England v New Zealand 2013.mp4"

output_wav_path = "F:/Software-Project/Sport-Highlights/Audios/audio2.wav"

conv = Convertor()
# Convert the video to WAV
conv.to_wav(input_video_path, output_wav_path)

print(f"Conversion complete. WAV file saved at: {output_wav_path}")