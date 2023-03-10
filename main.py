import requests
import geocoder

API_KEY = "2ad0cecd82b29f4b2e289b6777b1e49b"


def get_location():
    g = geocoder.ip('me')
    location = g.city
    return location, g.latlng


def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data


def format_output(location, weather_data):
    temperature_celsius = round(weather_data['main']['temp'] - 273.15, 2)
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_desc = weather_data['weather'][0]['description']
    output_string = f"You are currently in {location}. The current weather is {weather_desc}, the temperature is {temperature_celsius}°C, the humidity is {humidity}% and the wind speed is {wind_speed} m/s."
    return output_string


def main():
    location, (lat, lon) = get_location()
    weather_data = get_weather_data(lat, lon)
    output_string = format_output(location, weather_data)
    print(output_string)


if __name__ == '__main__':
    main()
