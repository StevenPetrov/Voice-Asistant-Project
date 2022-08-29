from main.tts_stt import speech_to_text, text_to_speech

actions = {
    'lights_on': ['turn', 'on', 'lights'],
    'lights_off': ['turn', 'off', 'lights'],
}


def main():
    while True:
        command = speech_to_text()
        if command is not None:
            return command


def check_if_command_recognized(command, actions):
    for action, text in actions.items():
        for x in text:
            if x not in command:
                return None
            return action


while True:
    main = main()
    com = check_if_command_recognized(main, actions)
    if com is not None:
        text_to_speech(com)
