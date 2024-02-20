import torch
import whisper
from transformers import pipeline
from datasets import load_dataset

# class Transcriptor:
#   def __init__(self):
#     device = "cuda:0" if torch.cuda.is_available() else "cpu"
#     self.pipe = whisperx.load_model('base')

#   def transcribe(self,path):
#     prediction = self.pipe(path, batch_size=8, return_timestamps=True)["chunks"]
#     print(prediction)

#     return prediction

pipe = whisper.load_model('base', device='cuda')
result = pipe.transcribe('F:\Software-Project\Highlights\Sports-highlights\Audios\\1708357021.792142.wav',task='translate')
print(result["segments"])