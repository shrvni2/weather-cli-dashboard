```python
import argparse
import json
import requests
from datetime import datetime
from tabulate import tabulate

from config import API_KEY, BASE_URL
from helpers import get_location, get_weather_data, parse_weather_data

def main():
    parser = argparse.ArgumentParser(description='Weather Dashboard')
    parser.add_argument('-l', '--location', help='Location (city, state, country)')
    parser.add_argument('-u', '--units', help='Units (metric, imperial)', default='metric')
    args = parser.parse_args()

    location = get_location(args.location)
    weather_data = get_weather_data(location, args.units, API_KEY, BASE_URL)
    parsed_data = parse_weather_data(weather_data)

    print(f"Weather in {location['name']}, {location['country']}")
    print(f"Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    table = [
        ["Description", parsed_data['description']],
        ["Temperature", f"{parsed_data['temperature']} {parsed_data['units']}"],
        ["Feels Like", f"{parsed_data['feels_like']} {parsed_data['units']}"],
        ["Humidity", f"{parsed_data['humidity']}%"],
        ["Wind Speed", f"{parsed_data['wind_speed']} {parsed_data['units']}/s"],
    ]

    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
```