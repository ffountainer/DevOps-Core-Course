"""
DevOps Info Service
Lab 1. Veronika Levasheva
"""

from flask import Flask, jsonify
from flask import request
import platform
from datetime import datetime
import socket
import os
import logging

app = Flask(__name__)  # creating an instance of Flask
logger = logging.getLogger(__name__)

# variable names
platform_name = platform.system()
architecture = platform.machine()
python_version = platform.python_version()
hostname = socket.gethostname()

# env variables
ADDRESS = os.getenv("ADDRESS", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"


# decorator for / path
@app.route("/", methods=["GET"])
def get_endpoint():
    logger.debug(f"Request: {request.method} {request.path}")
    response = jsonify(message=message)
    response.status_code = 200
    return response


# decorator for /health path
@app.route("/health")
def health():
    logger.debug(f"Request: {request.method} {request.path}")
    response = jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "uptime_seconds": get_uptime()["seconds"],
        }
    )
    response.status_code = 200
    return response


# error handling


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "Endpoint does not exist"}), 404


@app.errorhandler(500)
def internal_error(error):
    return (
        jsonify(
            {
                "error": "Internal Server Error",
                "message": "An unexpected error occurred",
            }
        ),
        500,
    )


start_time = datetime.now()


def get_uptime():
    delta = datetime.now() - start_time
    seconds = int(delta.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return {"seconds": seconds, "human": f"{hours} hours, {minutes} minutes"}


# json message with system and environment info
message = {
    "service": {
        "name": "devops-info-service",
        "version": "1.0.0",
        "description": "DevOps course info service",
        "framework": "Flask",
        "debug status": DEBUG,
    },
    "system": {
        "hostname": hostname,
        "platform": platform_name,
        "platform_version": "Ubuntu 24.04",
        "architecture": architecture,
        "cpu_count": 8,
        "python_version": python_version,
    },
    "runtime": {
        "uptime_seconds": get_uptime(),
        "uptime_human": "1 hour, 0 minutes",
        "current_time": "2026-01-07T14:30:00.000Z",
        "timezone": "UTC",
    },
    "request": {
        "client_ip": "127.0.0.1",
        "port": PORT,
        "user_agent": "curl/7.81.0",
        "method": "GET",
        "path": "/",
    },
    "endpoints": [
        {"path": "/", "method": "GET", "description": "Service information"},
        {"path": "/health", "method": "GET", "description": "Health check"},
    ],
}

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger.info("Application starting...")

if __name__ == "__main__":
    app.run(host=ADDRESS, port=PORT, debug=DEBUG)
