import requests
import math

from main.convertor_cyrillic_lto_latin import translate_to_cyrillic
from main.tts_stt import text_to_speech, text_to_speech_bg


def sound_response(city, temp, feels_like, wind, humidity, weather):
    weather_map = {
        'light rain' : ' е облачно с леки превалявания',
        'overcast clouds': 'е предимно облачно',
        'clear sky' : 'е тихо и спокойно',
        'broken clouds' : 'е с разкъсана облачност'
    }

    result = f'Времето в {city} {weather_map[weather]} като температурата е {temp:.0f} градуса, ' \
             f'усеща се като {feels_like:.0f} градуса, влажността на въздуха е {humidity} процента, ' \
             f'а скоростта на вятъра е около {math.floor(wind)} метра в секунда.'

    text_to_speech_bg(result)

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

        wind = response['wind']['speed']
        humidity = response['main']['humidity']
        weather = response['weather'][0]['description']
        city = city.split(',')[0]
        translate_to_cyrillic(city)
        sound_response(city, temp, feels_like, wind, humidity, weather)

    get_weather(api_key, city_name)
