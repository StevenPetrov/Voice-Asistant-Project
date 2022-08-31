from main.google_directions import google_map_directions
from main.tts_stt import speech_to_text, text_to_speech, speech_to_text_bg
from main.weather_services import weather_check

NAME_OF_VOICE_ASSISTANT = 'Jarvis'


def get_command_via_voice_assistant_name():
    while True:
        command_via_voice = speech_to_text()
        print(command_via_voice)
        if command_via_voice is not None and NAME_OF_VOICE_ASSISTANT in command_via_voice:
            text_to_speech("I'm here")
            tries = 0
            while tries < 3:
                command_via_voice = speech_to_text()
                tries += 1
                if command_via_voice is None:
                    print('None' + f'{tries}')
                else:
                    print(command_via_voice + f'{tries}')
                if command_via_voice is not None:
                    return command_via_voice
            # text_to_speech("Sorry I didnt get that")


class LightsControl:
    def __init__(self,command_via_voice):
        self.command_via_voice = command_via_voice

    actions = {
        'lights is on': ['turn', 'on', 'lights'],
        'lights is off': ['turn', 'off', 'lights'],
    }

    def mainloop(self):
        for action, text in self.actions.items():
            found = True
            for x in text:
                if x not in self.command_via_voice:
                    found = False
                    break
            if found:
                text_to_speech(action)
        return None


class WeatherCheck:
    def __init__(self,command_via_voice):
        self.command_via_voice = command_via_voice

    cities = ['Sofia', 'Varna', 'Plovdiv', 'Burgas',]
    command_check = ['what', 'weather']

    def city_get(self):
        for city in self.cities:
            if city in self.command_via_voice:
                return city
        return None

    def mainloop(self):
        city = self.city_get()
        if city is None:
            city = 'Sofia'
        found = True
        for word in self.command_check:
            if word not in self.command_via_voice:
                found = False
                break
        if found:
            weather_check(city)


def get_command_type(command_via_voice):
    command_type = None
    if 'light' in command_via_voice:
        command_type = 'lights'
        return command_type
    elif 'weather' in command_via_voice:
        command_type = 'weather'
        return command_type
    elif 'google' in command_via_voice or 'directions' in command_via_voice:
        command_type = 'directions'
        return command_type
    return command_type


def mainloop():
    while True:
        main_command = get_command_via_voice_assistant_name()
        type_of_command = get_command_type(main_command)
        if type_of_command is None:
            continue
        elif type_of_command == 'weather':
            WeatherCheck(main_command).mainloop()
        elif type_of_command == 'lights':
            LightsControl(main_command).mainloop()
        elif type_of_command == 'directions':
            google_map_directions()




mainloop()