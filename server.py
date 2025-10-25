'''from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='localhost', port=5000)
'''

# backend/server.py
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Backend is running. SocketIO ready."

@socketio.on('message')
def handle_message(msg):
    print("Message received:", msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    # use host='0.0.0.0' if you need other devices on the network to connect
    socketio.run(app, host='127.0.0.1', port=5000)
