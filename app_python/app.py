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
from pythonjsonlogger.json import JsonFormatter

app = Flask(__name__)  # creating an instance of Flask


logger = logging.getLogger(__name__)


# Log important events: startup, HTTP requests, errors
# Include context: method, path, status code, client IP

logHandler = logging.StreamHandler()
formatter = JsonFormatter(
    "levelname, asctime, message",
    style=",",
    rename_fields={"levelname": "LEVEL", "asctime": "TIMESTAMP", "message": "MESSAGE"},
)

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

logger.setLevel(logging.DEBUG)

# variable names
platform_name = platform.system()
architecture = platform.machine()
python_version = platform.python_version()
hostname = socket.gethostname()

# env variables
ADDRESS = os.getenv("ADDRESS", "0.0.0.0")
PORT = int(os.getenv("PORT", 1999))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"


# decorator for / path
@app.route("/", methods=["GET"])
def get_endpoint():
    logger.info(
        {
            "MESSAGE": f"Request: {request.method} {request.path}",
        },
        extra={
            "CLIENT_IP": request.remote_addr,
            "STATUS_CODE": 200,
            "METHOD": request.method,
            "PATH": request.path,
        },
    )
    response = jsonify(message=message)
    response.status_code = 200
    return response


# decorator for /health path
@app.route("/health")
def health():
    # extra: status code, client ip
    logger.info(
        {
            "MESSAGE": f"Request: {request.method} {request.path}",
        },
        extra={
            "CLIENT_IP": request.remote_addr,
            "STATUS_CODE": 200,
            "METHOD": request.method,
            "PATH": request.path,
        },
    )
    response = jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "uptime_seconds": get_uptime()["seconds"],
        }
    )
    response.STATUS_CODE = 200
    return response


# error handling


@app.errorhandler(404)
def not_found(error):
    logger.error(
        {"MESSAGE": "Endpoint does not exist"},
        extra={
            "ERROR": "Not Found",
            "STATUS_CODE": 404,
            "CLIENT_IP": request.remote_addr,
            "METHOD": request.method,
            "PATH": request.path,
        },
    )
    return (jsonify({"error": "Not Found", "MESSAGE": "Endpoint does not exist"}), 404)


@app.errorhandler(500)
def internal_error(error):
    logger.error(
        {"MESSAGE": "Internal Server Error"},
        extra={
            "ERROR": "Not Found",
            "STATUS_CODE": 404,
            "CLIENT_IP": request.remote_addr,
            "METHOD": request.method,
            "PATH": request.path,
        },
    )
    return (
        jsonify(
            {
                "error": "Internal Server Error",
                "MESSAGE": "An unexpected error occurred",
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

logger.info(
    {
        "MESSAGE": f"Application starting on port {PORT}...",
    }
)

if __name__ == "__main__":
    app.run(host=ADDRESS, port=PORT, debug=DEBUG)
