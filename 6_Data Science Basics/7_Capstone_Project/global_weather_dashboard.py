import requests
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

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
        print("Error fetching data:", response.status_code)
        return None

def forecast_7_day(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "cnt": 7,
        "units": "metric"
    }
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None


def display_7_day_weather_forecast(data):
    print(f"City: {data['name']}")
    for forecast in data['list']:
        print("\n--------------------")
        epoch = forecast['dt']
        week_day = datetime.fromtimestamp(epoch/1000).strftime("%A")
        date = datetime.fromtimestamp(epoch).strftime("%Y-%m-%d")
        print(f"Day of the week: {week_day}, {date}")
        print(f"Min Temperature: {forecast['temp']['min']}°C")
        print(f"Max Temperature: {forecast['temp']['max']}°C")
        print(f"Weather: {forecast['weather'][0]['description']}")
        print(f"Humidity: {forecast['humidity']}%")
        print(f"Wind Speed: {forecast['speed']} m/s")


def display_weather_data(data):
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    

def plot_weather_trend(days, temperatures):
    plt.plot(days, temperatures, marker='o', color='blue')
    plt.title("Temperature Trend")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.show()
    

def plot_wind_spe_cities(days, wind_speed, cities):
    fig = px.line()
    
    
def compare_weather(cities):
    temps = []
    for city in cities:
        data = fetch_weather_data(city)
        if data:
            temps.append((city, data['main']['temp']))

    # Plot comparison
    city_names = [t[0] for t in temps]
    city_temps = [t[1] for t in temps]
    plt.bar(city_names, city_temps, color='skyblue')
    plt.title("Temperature Comparison")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.show()
    

def main():
    print("Welcome to the Global Weather Dashboard!")
    while True:
        print("\nMenu:")
        print("1. View Weather for a City")
        print("2. Compare Weather for Multiple Cities")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            city = input("Enter the city name: ")
            weather_data = fetch_weather_data(city)
            if weather_data:
                display_weather_data(weather_data)
        elif choice == "2":
            cities = input("Enter city names separated by commas: ").split(",")
            compare_weather([city.strip() for city in cities])
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()