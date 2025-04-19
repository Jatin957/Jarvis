import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print(f"Your Buddy: {text}")
    engine.say(text)
    engine.runAndWait()
