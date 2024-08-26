#!/usr/bin/python3

from app import create_app, socketio

# Create an app instance using the app factory
app = create_app()

if __name__ == '__main__':
    # Run the app with SocketIO for handling real-time features
    sucketio.run(app, host'0.0.0.0', port=5000, debug=True)
