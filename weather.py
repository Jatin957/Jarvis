import requests
from speak_engine import speak

def get_weather(city_name="Chandigarh"):
    api_key = ""  # Replace with your actual API key
    lat = 30.7333
    lon = 76.7794
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url).json()
        if response["cod"] == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"The temperature in {city_name} is {temp} degrees Celsius with {desc}.")
        else:
            speak("City not found.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather right now.")
        print("Error:", e)
