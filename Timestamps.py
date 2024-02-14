from Whisper import transcription
from VidToAudio import vidAud
from LLM import gpt
import datetime

class Generator:
    def __init__(self) -> None:
        self.wav_path = "F:\Software-Project\Highlights\Sports-highlights\Audios\\"
        self.conv = vidAud.Convertor()
        self.trans = transcription.Transcriptor()
        self.llm = gpt.LLM()
    
    def get_highlight_timestamps(self,input_video_path):
        output_wav_path = f'{self.wav_path}{datetime.datetime.now().timestamp()}.wav'
        print('This is the path :',output_wav_path)
        self.conv.to_wav(input_video_path, output_wav_path)
        print(f"Conversion complete. WAV file saved at: {output_wav_path}")
        
        transcripts = self.trans.transcribe(output_wav_path)
        print(transcripts)
        print("Transcription done.. Sending to LLM")
        
        completion = self.llm.get_timestamps(transcripts)
        return completion["choices"][0]["message"]["content"]
        

if __name__=='main':

    input_video_path = "F:\Software-Project\Sport-Highlights\Cricket-data\DRAMATIC Final Over!   15 Runs To Win Off 6 Balls   West Indies v India   1st CG United ODI 2022.mp4"

    gen = Generator()
    completion = gen.get_highlight_timestamps(input_video_path)

    print(completion)