import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    api_key = "dae7873e1f85e2981b95486d5ee1e6a4"  # Replace with your OpenWeatherMap API Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return
        
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]
        
        # Update weather info
        result_label.config(text=f"Weather in {city_name}, {country}\n"
                                 f"Temperature: {temp}°C (Feels like {feels_like}°C)\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Wind Speed: {wind_speed} m/s\n"
                                 f"Condition: {weather.capitalize()}")
        
        # Fetch weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        img_data = icon_response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        icon_label.config(image=photo)
        icon_label.image = photo

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection.")

# Create GUI
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("400x400")
root.config(bg="#87CEEB")

title_label = tk.Label(root, text="🌦 Weather App 🌦", font=("Arial", 18, "bold"), bg="#87CEEB")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="#4682B4", fg="white")
search_button.pack(pady=5)

icon_label = tk.Label(root, bg="#87CEEB")
icon_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#87CEEB", justify="left")
result_label.pack(pady=10)

root.mainloop()
