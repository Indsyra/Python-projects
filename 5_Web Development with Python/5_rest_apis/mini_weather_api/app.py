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
    "sidney": {"temperature": 18, "condition": "Rainy"},
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

# Add New Weather Data
@app.route('/weather', methods=['POST'])
def add_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get('condition')

    if not city or not temperature or not condition:
        return jsonify({'error': 'Missing city, temperature or condition'}), 400

    weather_data[city] = {'temperature': temperature, 'condition': condition}
    return jsonify({'message': f'weather for {city} added successfully'}), 201

# Bonus Challenge: Add a PUT to update existing city weather, Add a DELETE to remove a city from the weather data
# Update a city
@app.route('/weather', methods=['PUT'])
def update_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get('condition')

    if not city or (not temperature and not condition):
        return jsonify({'error': 'City is mandatory for update. At least either temperature or condition should be provided'}), 400

    if city not in weather_data:
        return jsonify({"error": "City not found"}), 404

    if temperature:
        weather_data[city]['temperature'] = temperature
    if condition:
        weather_data[city]['condition'] = condition

    return jsonify({'message': f'weather for {city} updated successfully'}), 201


# Delete a city
@app.route('/weather', methods=['DELETE'])
def delete_city_weather():
    data = request.json
    city = data.get('city', '').lower()

    if not city:
        return jsonify({'error': 'City is mandatory for delete.'}), 400

    if city not in weather_data:
        return jsonify({"error": "City not found"}), 404

    weather_data.pop(city)

    return jsonify({'message': f'weather for {city} deleted successfully'}), 201


# Run App
if __name__ == '__main__':
    app.run(debug=True)