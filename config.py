```python
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['OPENWEATHERMAP']['API_KEY']
BASE_URL = config['OPENWEATHERMAP']['BASE_URL']
FOREX_API_KEY = config['FOREX']['API_KEY']
GEOCODER_API_KEY = config['GEOCODER']['API_KEY']

def load_config():
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as f:
            f.write('[OPENWEATHERMAP]\n')
            f.write('API_KEY = \n')
            f.write('BASE_URL = https://api.openweathermap.org/data/2.5/\n')
            f.write('\n')
            f.write('[FOREX]\n')
            f.write('API_KEY = \n')
            f.write('\n')
            f.write('[GEOCODER]\n')
            f.write('API_KEY = \n')
        print("Please fill in the API keys in the config.ini file.")
        exit(1)

load_config()
```