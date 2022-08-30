import requests
import math

from main.tts_stt import text_to_speech


def weather_check(city):
    city_name = f"{city}, BG"
    api_key = "5eea36078a11b457ba3d65a42045de3e"

    def get_weather(api_key, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(url).json()
        temp = response['main']['temp']
        temp = math.floor((temp * 1.8) - 459.67)
        temp -= 32
        temp *= 0.5556

        feels_like = response['main']['feels_like']
        feels_like = math.floor((feels_like * 1.8) - 459.67)
        feels_like -= 32
        feels_like *= 0.5556

        humidity = response['main']['humidity']
        city_name = city.split('.')[0]
        result = f'The temperature in {city_name} is {temp:.0f} degrees and the humidity is {humidity} percents'
        text_to_speech(result)


    get_weather(api_key, city_name)
