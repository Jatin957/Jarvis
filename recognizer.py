import speech_recognition as sr
import time
from speak_engine import speak

def take_command(retry_limit=3):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        time.sleep(0.5)
        audio = recognizer.listen(source)

    for attempt in range(retry_limit):
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            if attempt < retry_limit - 1:
                speak("Sorry, I didn't catch that. Could you say it again?")
                return take_command()
            else:
                speak("Sorry, I couldn't understand.")
                return "None"
        except Exception:
            speak("Something went wrong.")
            return "None"
