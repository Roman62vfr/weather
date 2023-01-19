from flask import Flask, render_template
import requests, json

app = Flask(__name__)


@app.route("/")
def get():
    r = requests.get("http://server:5000/status")
    json_data = json.loads(r.text)
    return render_template('index.html', data=json_data)

@app.route("/update")
def update():
    r = requests.get("http://server:5000/update")
    json_data = json.loads(r.text)
    print(json_data)
    return render_template('current.html', data=json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)