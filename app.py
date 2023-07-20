import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_timestamp_and_hostname():
    # Get the current timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the hostname
    hostname = socket.gethostname()

    # Prepare the response
    response = {
        'timestamp': timestamp,
        'hostname': hostname
    }

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
