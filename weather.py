import requests

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Error: Unable to fetch weather data"

# Replace 'your_api_key' with your actual WeatherAPI API key
api_key = 'b51c6c5ff6d341f8a0d01614241501'
city = 'Tokyo'

weather_data = get_weather(api_key, city)
print(f"Raw weather data:\n{weather_data}\n")

condition = weather_data['current']['condition']['text']
wind_speed = weather_data['current']['wind_mph']
wind_direction = weather_data['current']['wind_dir']

print(f"Summary:\n{condition}, wind speed {wind_speed} mph, direction '{wind_direction}'")

# print(weather_data)
