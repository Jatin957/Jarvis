import requests
from speak_engine import speak

def get_weather(city_name="Chandigarh"):
    api_key = ""  # 🔑 Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            speak(f"The temperature in {city_name} is {temp} degrees Celsius with {desc}.")
            speak(f"Humidity is {humidity} percent and wind speed is {wind_speed} meters per second.")
        else:
            speak("I couldn't find the city. Please try again.")
            print("API response:", data)

    except Exception as e:
        speak("Sorry, I couldn't fetch the weather right now.")
        print("Error:", e)

