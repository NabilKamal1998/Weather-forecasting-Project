import requests
import geocoder

api_key = "2ad0cecd82b29f4b2e289b6777b1e49b"
g = geocoder.ip('me')

lat, lon = g.latlng

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()

temperature_celsius = round(data['main']['temp'] - 273.15, 2)
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
weather_desc = data['weather'][0]['description']

print(f"The current weather where you are is {weather_desc}, the temperature is {temperature_celsius}°C, the humidity is {humidity}% and the wind speed is {wind_speed} m/s.")
