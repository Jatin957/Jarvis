import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def run_jarvis():
    greet()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I didn't understand that.")


run_jarvis()
