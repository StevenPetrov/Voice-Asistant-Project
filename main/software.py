from main.tts_stt import speech_to_text, text_to_speech
from main.weather_services import weather_check

actions = {
    'lights is on': ['turn', 'on', 'lights'],
    'lights is off': ['turn', 'off', 'lights'],
    'weather check Sofia': ['is', 'weather', 'Sofia'],
    'weather check Grigorevo': ['is', 'weather', 'Grigorevo'],
}


def main():
    while True:
        command = speech_to_text()
        print(command)
        if command is not None:
            # if 'Jarvis' in command:
                return command


def check_if_command_recognized(command, actions):
    for action, text in actions.items():
        found = True
        for x in text:
            if x not in command:
                found = False
                break
        if found:
            return action
    return None


while True:
    main_command = main()
    com = check_if_command_recognized(main_command, actions)
    if com is not None:
        if com == 'weather check Sofia':
            weather_check('Sofia')
        else:
            text_to_speech(com)
