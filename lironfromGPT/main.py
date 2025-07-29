from flask import Flask, request

app = Flask(__name__)

# GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return {'message': 'Hello from Flask!'}, 200

# POST endpoint
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return {'message': 'Received', 'data': data}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
