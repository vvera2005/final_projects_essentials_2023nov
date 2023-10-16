try:
    import requests
except ModuleNotFoundError:
    print("Go to terminal and write 'pip install requests'")
import json
import argparse

def get_weather(city):
    api_key = "a5ebcfe9d324fee906dbb6e1902dbfbb"
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    return weather_data.json()

def weather_dir(weather_data):
    md = {}
    md['temperature'] = weather_data["main"]["temp"]
    md['weather_description'] = weather_data['weather'][0]["description"]
    md['pressure'] = weather_data['main']['pressure']
    md['humidity'] = weather_data['main']['humidity']
    md['wind_speed'] = weather_data['wind']['speed']
    return md


def main():
    parser = argparse.ArgumentParser(description='Information conserning weather: ')
    parser.add_argument('city_name', type=str, help='Enter a city name: ')
    parser.add_argument('--par', type=str, help='Enter a+the weather  parametrs that you need: ', nargs="+")
    args = parser.parse_args()

    weather_data = get_weather(args.city_name)
    if weather_data['cod'] == '404':
        print("City not found")
        return None
    my_weather = weather_dir(weather_data)
    if args.par:
        for el in args.par:
            print(my_weather[el])
    else:
        print(my_weather)
    

main()
