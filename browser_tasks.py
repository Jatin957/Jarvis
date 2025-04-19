import os
import webbrowser
import pywhatkit
from speak_engine import speak

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_spotify():
    speak("Opening Spotify")
    webbrowser.open("https://open.spotify.com")

def open_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(chrome_path):
        speak("Opening Chrome")
        os.startfile(chrome_path)
    else:
        speak("Chrome is not installed in the default location.")

def play_on_youtube(song):
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)

def send_whatsapp(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+{number}", message)
    speak("Message sent!")
