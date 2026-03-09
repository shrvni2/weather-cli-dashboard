# 🌞 weather-cli-dashboard
A Python CLI app for displaying real-time weather data.

## 📝 Description
The weather-cli-dashboard is a command-line application built with Python that provides real-time weather data for a given location. It uses the OpenWeatherMap API to fetch the latest weather updates and displays the information in a user-friendly format.

## 🎯 Features
* Displays current weather conditions for a specified location
* Supports multiple units of measurement (metric, imperial)
* Provides detailed weather information, including temperature, feels-like temperature, and description
* Updates in real-time using the OpenWeatherMap API

## 🛠️ Tech Stack
* Python 3.x
* OpenWeatherMap API
* requests library for API calls
* tabulate library for formatting output
* argparse library for parsing command-line arguments

## 📦 Installation
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
Make sure to replace the `API_KEY` variable in `config.py` with your own OpenWeatherMap API key.

## 🚀 Usage
To run the weather-cli-dashboard, use the following command:
```bash
python weather_dashboard.py -l <location> -u <units>
```
Replace `<location>` with the city, state, or country for which you want to retrieve the weather data, and `<units>` with the desired unit of measurement (metric or imperial).

## 🗂️ Project Structure
* `weather_dashboard.py`: The main application file
* `config.py`: Configuration file containing the OpenWeatherMap API key and base URL
* `weather_api.py`: Module for interacting with the OpenWeatherMap API
* `utils.py`: Module containing helper functions for parsing and formatting weather data
* `tests/test_main.py`: Unit tests for the main application
* `requirements.txt`: List of dependencies required by the application
* `.gitignore`: File specifying files and directories to ignore in the Git repository

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/shrvni2/weather-cli-dashboard/blob/main/LICENSE) file for details.