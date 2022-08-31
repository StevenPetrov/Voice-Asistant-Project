import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say('Welcome to Medium')
engine.runAndWait()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")