import datetime as dt
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

while True:
    print('')
    inp=input("City: ")

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "886705b4c1182eb1c69f28eb8c520e20"
    CITY = inp.capitalize()



    def kelvin_to_celcius_fahrenheit(kelvin):
        celsius = kelvin - 272.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celcius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celcius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


    print('')
    print(f"WEATHER IN {Fore.RED}{CITY.upper()}")
    print('\n')
    print(f'Temperature in {CITY}: {temp_celcius:.2f}°C')
    print(f'Temperature in {CITY} feels like: {feels_like_celcius:.2f}°C')
    print(f'Wind Speed in {CITY}: {wind_speed}m/s')
    print(f'Humidity in {CITY}: {humidity}%')
    print(f'General Weather in {CITY}: {description.capitalize()}')
    print(Fore.YELLOW + f'Sun rises in {CITY}{Fore.YELLOW} at {sunrise_time} local time.')
    print(f'Sun sets in {CITY} at {sunset_time} local time.\n')

