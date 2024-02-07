from Timestamps import Generator
from flask import Flask, jsonify, request


gen = Generator()

app = Flask(__name__)

data = []  # Store data for the API
timestamps = None
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    req = request.get_json()
    vid_path = req['path']
    timestamps = gen.get_highlight_timestamps(vid_path)    
    data.append(timestamps)
    return '', 204  # No content response

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging for development
