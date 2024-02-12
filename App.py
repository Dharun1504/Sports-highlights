from Timestamps import Generator
import json
from videoGen.videoGenerate import cut_video
import datetime
gen = Generator()

class SportApp:
    def __init__(self):
        self.destination = "F:\Software-Project\Highlights\Sports-highlights\Destination\\"
    
    def make(self,in_path):
# in_path="F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Sharma Stars In Thriller   SUPER OVER REPLAY   BLACKCAPS v India - 3rd T20, 2020.mp4"
        timestamps = gen.get_highlight_timestamps(in_path)  
        print(timestamps)
        j = json.loads(timestamps)  
        print(j)
        op = f'{self.destination}{datetime.datetime.now().timestamp()}.mp4'
        cut_video(in_path,op,j)
        return op
        
# app = SportApp()
# app.make("F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Pakistan Need 2 Runs in 6 Ball   Most Shocking & Thrilling Last Over   PAK vs Australia   PCB M1C2.mp4")
