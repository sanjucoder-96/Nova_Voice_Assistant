import os
import requests

def get_weather_update(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key not found. Please set OPENWEATHER_API_KEY as an environment variable."

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        return f"The temperature in {city} is {temp}°C with {weather_desc}. Humidity is {humidity}%."
    else:
        return "Sorry, I couldn't fetch the weather for that location."
