import openai
from speak_engine import speak

# Replace with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

def talk_to_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        reply = response['choices'][0]['message']['content']
        speak(reply)
        return reply
    except Exception as e:
        error_msg = "Sorry, I couldn't connect to OpenAI right now."
        speak(error_msg)
        print("OpenAI Error:", e)
        return error_msg
