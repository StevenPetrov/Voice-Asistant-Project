import urllib.request, json
import time

from main.convertor_cyrillic_lto_latin import translate_to_latin
from main.tts_stt import speech_to_text, text_to_speech, speech_to_text_bg, text_to_speech_bg


def google_map_directions():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = ''

    origin = ('Sofia, vitinya 14b').replace(' ','+')

    tries = 0

    while tries < 2:
        text_to_speech_bg('До кой град желаете да пътувате?')
        dest_city = translate_to_latin(speech_to_text_bg())
        print(dest_city)
        if dest_city is not None:
                time.sleep(1)
                text_to_speech_bg('До коя улица?')
                dest_street_cyrillic = speech_to_text_bg()
                dest_street = translate_to_latin(dest_street_cyrillic)
                print(dest_street)
                if dest_street is not None:
                    destination = f'{dest_city}, {dest_street}'
                    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination.replace(' ','+'),api_key)
                    request = endpoint + nav_request

                    response = urllib.request.urlopen(request).read()
                    try:
                        directions = json.loads(response)
                        distance =(directions['routes'][0]['legs'][0]['distance']['text']).split(' ')[0]
                        time_info = (directions['routes'][0]['legs'][0]['duration']['text'])
                        if len(time_info) > 2:
                            hours = time_info.split(' ')[0]
                            mins = time_info.split(' ')[2]
                            if hours == '1':
                                time_info = f"{hours} час и {mins} минути."
                            else:
                                time_info = f"{hours} часа и {mins} минути."
                        else:
                            time_info = f"{time_info.split(' ')[0]} минути."
                        text_to_speech_bg(f'Разстоянието до улица {dest_street_cyrillic} e {distance} километра, а времето за достигането й е {time_info}') # {dest_street}
                        break
                    except IndexError:
                        text_to_speech_bg(f'Съжалявам, но не успях да намеря маршерут до тази локация.')
        tries += 1
