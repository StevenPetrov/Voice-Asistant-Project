from main.convertor_cyrillic_lto_latin import translate_to_latin
from main.google_directions import google_map_directions
from main.news_catcher5 import news_scrapper
from main.tts_stt import speech_to_text, text_to_speech, speech_to_text_bg
from main.weather_services import weather_check

NAME_OF_VOICE_ASSISTANT = 'Виктория'


def get_command_via_voice_assistant_name():
    while True:
        command_via_voice = speech_to_text_bg()
        print(command_via_voice)
        if command_via_voice is not None and NAME_OF_VOICE_ASSISTANT in command_via_voice:
            text_to_speech("I'm here")
            tries = 0
            while tries < 3:
                command_via_voice = speech_to_text_bg()
                tries += 1
                if command_via_voice is None:
                    print('None' + f'{tries}')
                else:
                    print(command_via_voice + f'{tries}')
                if command_via_voice is not None:
                    return command_via_voice


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


def weather_check_info_get(main_command):
    command = main_command

    def city_get(command):
        city = command.split(' ')[-1]
        return city

    def mainloop(command):
        city = city_get(command)
        latin_city = translate_to_latin(city)
        weather_check(latin_city)

    mainloop(command)


def get_command_type(command_via_voice):
    command_type = None
    if 'light' in command_via_voice:
        command_type = 'lights'
        return command_type
    elif 'време' in command_via_voice:
        command_type = 'weather'
        return command_type
    elif 'стартирай' in command_via_voice or 'навигация' in command_via_voice:
        command_type = 'directions'
        return command_type
    elif 'новини' in command_via_voice:
        command_type = 'news'
        return command_type
    return command_type


def mainloop():
    while True:
        main_command = get_command_via_voice_assistant_name()
        type_of_command = get_command_type(main_command)
        if type_of_command is None:
            continue
        elif type_of_command == 'weather':
            weather_check_info_get(main_command)
        elif type_of_command == 'lights':
            LightsControl(main_command).mainloop()
        elif type_of_command == 'directions':
            google_map_directions()
        elif type_of_command == 'news':
            news_scrapper()

mainloop()