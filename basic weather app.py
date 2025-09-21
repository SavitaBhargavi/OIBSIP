import requests

def get_weather(city):
    API_KEY = "dae7873e1f85e2981b95486d5ee1e6a4"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Condition: {weather['description'].capitalize()}")
    else:
        print("❌ City not found or API request failed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
