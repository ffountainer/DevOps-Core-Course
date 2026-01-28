# User-facing documentation

## Overview 

When acessed, this web service answers with information either about itself (path "/") or with its health status ("/health). The information includes fields with the details of the service, system, runtime, request and enpoints. 

## Prerequisites

### Python version

Pyenv is used for the virtual environment managing. To install it refer to [this website](https://akrabat.com/creating-virtual-environments-with-pyenv/) for instructions.

Python version used: 3.12.9


### Python libraries:
- jsonify imported from Flask library
- request imported from Flask library
- platform
- socket
- datetime imported from datetime
- os
- logging

### Installation

```bash
pyenv virtualenv 3.12.9 webapp
pyenv activate webapp
pip install -r requirements.txt
   ```
### Running the Application
```bash
python app.py
PORT=8080 python app.py # if you want to use a custom port (the default is 5000)
```

### API Endpoints ###
- `GET /` - Service and system information
- `GET /health` - Health check

### Configuration ###

| №  | Var name | Description 
| ---| ----- | --------------------|
| #1 | HOST | Name of the host (defaults to socket.hostname first if available) | 
| #2 | PORT | Port for the application access | 
| #3 | DEBUG | Debug status | 

