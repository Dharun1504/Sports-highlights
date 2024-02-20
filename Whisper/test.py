from transcription import Transcriptor

trans = Transcriptor()

wav_path = "F:\Software-Project\Highlights\Sports-highlights\Audios\\1708357021.792142.wav"
print(wav_path)
transcription = trans.transcribe(wav_path)
print(transcription)