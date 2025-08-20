# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
import time

# Initialize the Flask application
app = Flask(__name__)

# This is the crucial part for cross-container communication.
# It allows requests from any origin.
CORS(app)


@app.route('/')
def front_page():
    return """
    <html>
        <head>
            <title>Flask Front Page</title>
            <style>
                body {
                    background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
                    font-family: 'Segoe UI', Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 700px;
                    margin: 60px auto;
                    background: #fff;
                    border-radius: 16px;
                    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                    padding: 40px;
                    text-align: center;
                }
                h1 {
                    color: #4f46e5;
                    margin-bottom: 16px;
                }
                p {
                    color: #374151;
                    font-size: 1.2em;
                }
                .info {
                    margin-top: 32px;
                    padding: 18px;
                    background: #f1f5f9;
                    border-radius: 8px;
                    color: #2563eb;
                    font-weight: 500;
                }
                .footer {
                    margin-top: 40px;
                    font-size: 0.95em;
                    color: #64748b;
                }
                a {
                    color: #6366f1;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Flask Front Page!</h1>
                <p>This is the front page served by Flask.</p>
                <div class="info">
                    <strong>Docker Compose Demo:</strong><br>
                    This backend is running in a Docker container.<br>
                    Try accessing the <a href="/api/data">API endpoint</a> to see JSON data.
                </div>
                <div class="footer">
                    &copy; 2024 Flask Demo | <a href="https://flask.palletsprojects.com/">Learn more about Flask</a>
                </div>
            </div>
        </body>
    </html>
    """


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
