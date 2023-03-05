from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def home():
    ip = requests.get("https://ifconfig.me")
    ip = ip.text
    return ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, threaded=True)
