from flask import Flask, request, Response, render_template
from datetime import datetime

app = Flask(__name__)

# Log file path
LOG_FILE = "app.log"

# Function to log endpoint hits
def log_message(endpoint):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()} - {endpoint} endpoint was accessed\n")

# Endpoint: /your_name
@app.route('/your_name')
def your_name():
    log_message("/your_name")
    name = request.args.get('name', '<your_name>')  # Get 'name' from query string, default to '<your_name>'
    return f"Hello world from {name}!"

# Endpoint: /datetime
@app.route('/datetime')
def current_datetime():
    log_message("/datetime")
    now = datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# Endpoint: /log
@app.route('/log')
def view_log():
    log_message("/log")
    try:
        with open(LOG_FILE, "r") as log_file:
            logs = log_file.read()
        return Response(logs, mimetype="text/plain")
    except FileNotFoundError:
        return "Log file not found. No logs available yet."

# Endpoint: /
@app.route('/')
def landing():
    log_message("/")
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000) 