from transcription import Transcriptor

trans = Transcriptor()

wav_path = "F:\Software-Project\Sport-Highlights\Audios\dhoni.wav"

transcription = trans.transcribe(wav_path)
print(transcription)