from SportStack import Highlights_gemini, Highlights_gpt
import dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

sport = Highlights_gpt('react\\public\\Videos\\',
                          api_base="https://openai-demetrius.openai.azure.com/", 
                          api_version="2023-07-01-preview", 
                          api_key=dotenv.get_key(key_to_get="OPENAI_API_KEY", dotenv_path = ".env") )
# Highlightgen = Highlights_gemini('Destination\\',api_key=dotenv.get_key(key_to_get="GOOGLE_API_KEY", dotenv_path = ".env"))
# Highlightgen.generate_highlights('F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Every Ball of the Extraordinary Final Over at Lord\'s!   England v Sri Lanka 2014.mp4')

app = Flask(__name__)
CORS(app, origins = ['http://localhost:3000'])


data = []  # Store data for the API
timestamps = None
# @app.route('/data', methods=['GET'])
# def get_data():
#     return jsonify(data)

@app.route('/data', methods=['POST'])
@cross_origin()
def add_data():
    req = request.get_json()
    vid_path = req['path']
    print(vid_path)
    result = sport.generate_highlights(vid_path)    
    
    return jsonify(result), 200  # No content response

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging for development
