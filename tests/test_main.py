```python
import pytest
import json
import requests
from unittest.mock import patch, MagicMock
from weather_dashboard import main, get_location, get_weather_data, parse_weather_data
from config import API_KEY, BASE_URL
from weather_api import WeatherAPI

def test_main():
    with patch('argparse.ArgumentParser') as mock_argparse:
        mock_argparse.return_value.parse_args.return_value = MagicMock(location='London', units='metric')
        main()

def test_get_location():
    assert get_location('London') == {'name': 'London', 'country': 'UK'}

def test_get_weather_data():
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    weather_data = weather_api.get_weather_data('London', 'metric')
    assert weather_data is not None

def test_parse_weather_data():
    weather_data = {
        'main': {
            'temp': 20,
            'feels_like': 18,
            'humidity': 60,
            'temp_min': 15,
            'temp_max': 25
        },
        'weather': [
            {'description': 'sunny'}
        ],
        'wind': {
            'speed': 5
        }
    }
    parsed_data = parse_weather_data(weather_data)
    assert parsed_data['description'] == 'sunny'
    assert parsed_data['temperature'] == 20
    assert parsed_data['feels_like'] == 18
    assert parsed_data['humidity'] == 60
    assert parsed_data['wind_speed'] == 5

def test_get_weather_data_error():
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        weather_data = weather_api.get_weather_data('London', 'metric')
        assert weather_data is None

def test_parse_weather_data_error():
    weather_data = None
    with pytest.raises(TypeError):
        parse_weather_data(weather_data)

def test_main_error():
    with patch('argparse.ArgumentParser') as mock_argparse:
        mock_argparse.return_value.parse_args.return_value = MagicMock(location=None, units='metric')
        with pytest.raises(AttributeError):
            main()

def test_config_load():
    import os
    if os.path.exists('config.ini'):
        os.remove('config.ini')
    from config import load_config
    load_config()
    assert os.path.exists('config.ini')

def test_weather_api_init():
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    assert weather_api.api_key == API_KEY
    assert weather_api.base_url == BASE_URL

def test_weather_api_get_weather_data():
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'main': {'temp': 20}}
        weather_data = weather_api.get_weather_data('London', 'metric')
        assert weather_data == {'main': {'temp': 20}}

def test_weather_api_get_forecast_data():
    weather_api = WeatherAPI(API_KEY, BASE_URL)
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'main': {'temp': 20}}
        forecast_data = weather_api.get_forecast_data('London', 'metric')
        assert forecast_data == {'main': {'temp': 20}}
```