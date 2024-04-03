from Timestamps import Generator_gpt
import json
from videoGen.videoGenerate import cut_video
import datetime
from Timestamps import Generator_gemini

class Highlights_gpt:

    def __init__(self, destination, api_base, api_version, api_key):
        self.destination = destination
        self.gen = Generator_gpt(api_base, api_version, api_key)

    def generate_highlights(self, in_path, user_query):
        # in_path="F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Sharma Stars In Thriller   SUPER OVER REPLAY   BLACKCAPS v India - 3rd T20, 2020.mp4"
        timestamps = self.gen.get_highlight_timestamps(in_path,user_query)
        print(timestamps)
        j = json.loads(timestamps)
        print(j)
        name = datetime.datetime.now().timestamp()
        op = f'{self.destination}\{name}.mp4' 
        cut_video(in_path, op, j)
        return name
    
class Highlights_gemini:

    def __init__(self, destination,api_key):
        self.destination = destination
        self.gen = Generator_gemini(api_key)

    def generate_highlights(self, in_path):
        # in_path="F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Sharma Stars In Thriller   SUPER OVER REPLAY   BLACKCAPS v India - 3rd T20, 2020.mp4"
        timestamps = self.gen.get_highlight_timestamps(in_path)
        print(timestamps)
        j = json.loads(timestamps)
        print(j)
        op = f'{self.destination}{datetime.datetime.now().timestamp()}.mp4'
        cut_video(in_path, op, j)
        return op

# app = SportApp()
# app.make("F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Pakistan Need 2 Runs in 6 Ball   Most Shocking & Thrilling Last Over   PAK vs Australia   PCB M1C2.mp4")
