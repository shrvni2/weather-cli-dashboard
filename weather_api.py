```python
import requests
import json
from config import API_KEY, BASE_URL

class WeatherAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_weather_data(self, location, units):
        params = {
            'q': location,
            'units': units,
            'appid': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_forecast_data(self, location, units):
        params = {
            'q': location,
            'units': units,
            'appid': self.api_key
        }
        response = requests.get(self.base_url + '/forecast', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

def get_weather_data(location, units):
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    return weather_api.get_weather_data(location, units)

def get_forecast_data(location, units):
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    return weather_api.get_forecast_data(location, units)
```