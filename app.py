# app.py
from flask import Flask
import os

app = Flask(__name__)

# Load configuration from environment variables
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-default-secret-key')

@app.route('/api')
def hello_world():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
