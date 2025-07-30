from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Using weather API to fetch Data
API_KEY = "a7b9a036133578abcbe245cadff3e82c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast/daily"

def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def parse_weather(data):
    city = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    return {
        "city": city,
        "temperature": temperature,
        "description": description,
        "humidity": humidity,
        "wind_speed": wind_speed
    }
    

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        data = fetch_weather_data(city)
        if data:
            weather = parse_weather(data)
    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    app.run(debug=True)