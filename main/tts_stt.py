import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


def text_to_speech_bg(text):
    language = 'bg'
    command = gTTS(text, lang=language, slow=False)
    command.save("command.mp3")
    playsound("command.mp3")
    os.remove("command.mp3")


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # text_to_speech("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)  # language='bg'
            print("You said : {}".format(text))
            return text
        except:
            # print("Sorry could not recognize what you said")
            return None


def speech_to_text_bg():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text_to_speech("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='bg')
            print("You said : {}".format(text))
            return text
        except:
            # print("Sorry could not recognize what you said")
            return None


text_to_speech_bg('Йоничка ти си сладичка')