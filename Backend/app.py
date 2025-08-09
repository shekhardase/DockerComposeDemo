# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
import time

# Initialize the Flask application
app = Flask(__name__)

# This is the crucial part for cross-container communication.
# It allows requests from any origin.
CORS(app)

@app.route('/api/data')
def get_data():
    """
    This is the API endpoint. It returns a simple JSON payload.
    """
    return jsonify({
        'message': 'Hello from the Python Flask Backend!',
        'timestamp': int(time.time())
    })

if __name__ == '__main__':
    # We run on port 5000 and host 0.0.0.0 to make it accessible
    # from outside the container.
    app.run(host='0.0.0.0', port=5000)
