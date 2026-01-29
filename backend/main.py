from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "backend"
    })

@app.get("/api/message")
def message():
    return jsonify({
        "message": "Hello from Backend API (Flask)!"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
