from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    return jsonify({
        "project": "CloudDeploy",
        "message": "DevOps deployment platform is running!",
        "environment": ENVIRONMENT
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


@app.route("/running")
def status():
    return jsonify({
        "application": "CloudDeploy",
        "status": "running",
        "version": VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)