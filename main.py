import datetime
import time
import wikipedia
import pyjokes

from speak_engine import speak
from recognizer import take_command
import computer_tasks
import browser_tasks
import weather
import memory

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
                browser_tasks.play_on_youtube(song)

        elif 'time' in query:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time_now}")

        elif 'date' in query:
            today = datetime.date.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}")

        elif 'open google' in query:
            browser_tasks.open_google()

        elif 'open youtube' in query:
            browser_tasks.open_youtube()

        elif 'open spotify' in query:
            browser_tasks.open_spotify()

        elif 'open chrome' in query:
            browser_tasks.open_chrome()

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'weather' in query:
            speak("Which city's weather would you like to know?")
            city = take_command()
            if city != "None":
                weather.get_weather(city)

        elif 'send whatsapp' in query:
            speak("Tell me the phone number including country code")
            number = take_command().replace(" ", "")
            speak("What should I say?")
            message = take_command()
            browser_tasks.send_whatsapp(number, message)

        elif 'open notepad' in query:
            computer_tasks.open_notepad()

        elif 'open calculator' in query:
            computer_tasks.open_calculator()

        elif 'open file explorer' in query:
            computer_tasks.open_file_explorer()

        elif 'screenshot' in query:
            computer_tasks.take_screenshot()

        elif 'remember' in query:
            speak("What should I remember?")
            data = take_command()
            memory.remember(data)

        elif 'what do you remember' in query:
            memory.recall()

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
  run_your_buddy()

