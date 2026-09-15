from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "app": "NIFTY Market Direction App",
        "direction": "WAIT"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
