import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os
import requests
import pyautogui
import time

# Initialize voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

def speak(text):
    print(f"Your Buddy: {text}")
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
    time.sleep(0.5)
    speak("I am Your Buddy.")
    time.sleep(0.5)
    speak("How can I help you today?")

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
        except Exception as e:
            speak("Something went wrong.")
            return "None"

def get_weather(city):
    api_key = "your_openweather_api_key"  # replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response["cod"] == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}.")
        else:
            speak("City not found.")
    except:
        speak("Sorry, I couldn't fetch the weather right now.")

def run_your_buddy():
    greet()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("What should I search on Wikipedia?")
            topic = take_command()
            speak("Searching Wikipedia...")
            result = wikipedia.summary(topic, sentences=2)
            print(result)
            speak(result)

        elif 'play' in query and 'youtube' in query:
            speak("Which song do you want me to play?")
            song = take_command()
            if song != "None":
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

        elif 'time' in query:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time_now}")

        elif 'date' in query:
            today = datetime.date.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                speak("Opening Chrome")
                os.startfile(chrome_path)
            else:
                speak("Chrome is not installed in the default location.")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'weather' in query:
            speak("Which city's weather would you like to know?")
            city = take_command()
            if city != "None":
                get_weather(city)

        elif 'send whatsapp' in query:
            speak("Tell me the phone number including country code")
            number = take_command().replace(" ", "")
            speak("What should I say?")
            message = take_command()
            pywhatkit.sendwhatmsg_instantly(f"+{number}", message)
            speak("Message sent!")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            os.system("calc.exe")

        elif 'open file explorer' in query:
            speak("Opening File Explorer")
            os.system("explorer.exe")

        elif 'screenshot' in query:
            speak("Taking screenshot")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved.")

        elif 'remember' in query:
            speak("What should I remember?")
            data = take_command()
            with open("data.txt", "w") as f:
                f.write(data)
            speak("Got it. I’ll remember that.")

        elif 'what do you remember' in query:
            try:
                with open("data.txt", "r") as f:
                    memory = f.read()
                    speak(f"You asked me to remember: {memory}")
            except:
                speak("I don't remember anything yet.")

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I didn't understand that.")

# Start Your Buddy
run_your_buddy()
