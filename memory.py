from speak_engine import speak

def remember(data):
    with open("data.txt", "w") as f:
        f.write(data)
    speak("Got it. I’ll remember that.")

def recall():
    try:
        with open("data.txt", "r") as f:
            memory = f.read()
            speak(f"You asked me to remember: {memory}")
    except:
        speak("I don't remember anything yet.")
