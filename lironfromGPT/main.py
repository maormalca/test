import os
import logging
from flask import Flask, request

# Set up logging
log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    logging.debug('Handling GET request to /hello')
    # Log the request details
    logging.info('GET /hello - Returning Hello message')
    return {'message': 'Hello from Flask!'}, 200

# POST endpoint
@app.route('/submit', methods=['POST'])
def submit():
    logging.debug('Handling POST request to /submit')
    data = request.json
    logging.info('POST /submit - Received data: %s', data)
    logging.debug('POST /submit - Sending response')
    return {'message': 'Received', 'data': data}, 200

if __name__ == '__main__':
    # Run the app with the configured log level
    app.run(debug=True, host='0.0.0.0', port=5000)

