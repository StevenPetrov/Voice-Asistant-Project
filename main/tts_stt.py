import pyttsx3
import speech_recognition as sr


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
        # text_to_speech("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='bg')
            print("You said : {}".format(text))
            return text
        except:
            # print("Sorry could not recognize what you said")
            return None
