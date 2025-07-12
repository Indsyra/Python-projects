# REST APIs definition: Representational State Transfer
# Use HTTP methods to interact with resources
# Build APIs for Data Access, Scalability, Flexibility

# Setting up a Flask REST API
# pip install flask flask-restful

from flask import Flask, jsonify

app = Flask(__name__)

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Mini Weather API"})


if __name__ == '__main__':
    app.run(debug=True)