import pyttsx3
import speech_recognition as sr


def text_to_speach(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # text_to_speach("Speak Anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")


while True:
    command = speech_to_text()
    if command is not None:
        if 'hello' in command and 'Jarvis' in command:
            text_to_speach('I am ready for your commands')
            break