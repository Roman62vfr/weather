from flask import Flask, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

history = {}

@app.route('/status', methods=['GET'])
def get_list():
    return history

@app.route('/update', methods=['GET'])
def update():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?id=500096&units=metric&appid=60b08e562616b11011f251c220b1f738&lang=ru")
    data = json.dumps(response.json())
    jsondata = json.loads(data)
    weather = jsondata['weather'][0]['description']
    t = jsondata['main']['temp']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weather_data = {'weather': weather, 't': t}
    new_data = {timestamp: weather_data}
    history.update(new_data)
    return new_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)