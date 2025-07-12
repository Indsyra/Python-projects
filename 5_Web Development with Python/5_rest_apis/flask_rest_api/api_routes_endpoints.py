# REST APIs definition: Representational State Transfer
# Use HTTP methods to interact with resources
# Build APIs for Data Access, Scalability, Flexibility

# Setting up a Flask REST API
# pip install flask flask-restful

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock weather Data
weather_data = {
    "new york": {"temperature": 22, "condition": "Sunny"},
    "london": {"temperature": 15, "condition": "Cloudy"},
    "tokyo": {"temperature": 28, "condition": "Clear"},
}

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Mini Weather API"})

# Get Weather for all cities
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

# Get Weather for a specific city
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404

# Run App
if __name__ == '__main__':
    app.run(debug=True)