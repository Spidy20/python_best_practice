import pyttsx3

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

name = input("Enter name: ")
speak("Welcome back "+name)