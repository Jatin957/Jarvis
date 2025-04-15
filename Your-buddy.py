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

# Initialize voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

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
    speak("I am Your Buddy. How can I help you today?")

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
    except Exception:
        speak("Say that again please...")
        return "None"
    return query.lower()

def get_weather(Chandigarh):
    api_key = "1234567890abcdef1234567890abcdef"  # Replace this with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Chandigarh&appid=YOUR_API_KEY&units=metric"
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
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

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
            speak("Which city's weather do you want?")
            city = take_command()
            get_weather("Chandigarh")

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
            speak("I will remember that.")

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
