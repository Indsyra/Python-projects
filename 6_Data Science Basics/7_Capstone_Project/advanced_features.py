# Fetching Real-Time Weather Data
import requests
import matplotlib.pyplot as plt

API_KEY = "a7b9a036133578abcbe245cadff3e82c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

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
    
city_weather = fetch_weather_data("antibes")


# Visualizing Weather Trends
def display_weather_data(data):
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    
display_weather_data(city_weather)

def plot_weather_trend(days, temperatures):
    plt.plot(days, temperatures, marker='o', color='blue')
    plt.title("Temperature Trend")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.show()
    
    
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
    
    
# User-friendly Dashboard
def main():
    print("Welcome to the Global Weather Dashboard!")
    city = input("Enter the city name: ")
    
    weather_data = fetch_weather_data(city)
    if weather_data:
        display_weather_data(weather_data)
        
        # Simulated data for trend visualization
        days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
        temperatures = [22, 24, 23, 25, 26]
        plot_weather_trend(days, temperatures)
        
    else:
        print("Could not retrieve weather data. Please try again.")


if __name__ == "__main__":
    compare_weather(["Antibes", "Yaounde", "Paris"])

# Enhancing functionality with advanced features