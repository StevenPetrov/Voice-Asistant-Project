import urllib.request, json

from main.tts_stt import speech_to_text, text_to_speech, speech_to_text_bg


def google_map_directions():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = ''

    origin = ('Sofia, vitinya 14b').replace(' ','+')

    tries = 0

    while tries < 5:
        text_to_speech('To which city you want to travel?')
        dest_location = speech_to_text()
        text_to_speech(f'The city is {dest_location} correct?')
        confirmation = speech_to_text()
        if confirmation is not None:
            if 'yes' in confirmation:
                text_to_speech('To which street you want to travel?')
                dest_street = speech_to_text()
                text_to_speech(f'The street is {dest_street} correct?')
                confirmation = speech_to_text()
                if 'yes' in confirmation:
                    destination = f'Sofia, {dest_street}'
                    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination.replace(' ','+'),api_key)
                    request = endpoint + nav_request

                    response = urllib.request.urlopen(request).read()
                    try:
                        directions = json.loads(response)
                        distance =(directions['routes'][0]['legs'][0]['distance']['text'])
                        time = (directions['routes'][0]['legs'][0]['duration']['text'])
                        text_to_speech(f'The distance is {distance} and the time needed to reach this address is {time}') # {dest_street}
                        break
                    except IndexError:
                        text_to_speech("Sorry, but i couldn't find a route to this street.")
        tries += 1
