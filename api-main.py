from SportStack import SportApp
from flask import Flask, jsonify, request

sport = SportApp()

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
    result = sport.make(vid_path)    
    data.append(result)
    return '', 204  # No content response

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging for development
