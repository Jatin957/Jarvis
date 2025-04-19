import requests
from speak_engine import speak

def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace this
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
