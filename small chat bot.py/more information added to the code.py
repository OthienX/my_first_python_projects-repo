import random
import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser

# Define a list of greetings and corresponding responses
greetings = ['hello', 'hi', 'hey', 'greetings']
responses = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']

# Define custom commands and their corresponding actions/responses
custom_commands = {
    'help': "I am just a simple bot created with Python.",
    'info': "I wish I could help you with what you need.",
    'your_command': "This is the response to your custom command.",
    'time': str(datetime.datetime.now().time()),
    'greet_name': "Hello, [your_name]! How can I assist you?",
    'calculate_age': "I'm sorry, I cannot calculate your age.",
    'joke': "Why don't scientists trust atoms? Because they make up everything!"
}

# Create a recognizer object
recognizer = sr.Recognizer()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Main loop to handle user input
while True:
    # Get user input using the microphone
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using the Google Speech Recognition API
        user_input = recognizer.recognize_google(audio)
        print("User:", user_input)

        # Convert user input to lowercase
        user_input = user_input.lower()

        # Check if user input is a command
        if user_input.startswith('\\'):
            # Process different commands
            if any(command in user_input for command in custom_commands):
                if 'weather' in user_input:
                    # Extract the location from the user input
                    location = user_input.replace('weather', '').strip()
                    if location:
                        # Fetch weather information using the OpenWeatherMap API
                        api_key = "YOUR_API_KEY"
                        base_url = "https://api.openweathermap.org/data/2.5/weather"
                        params = {
                            "q": location,
                            "appid": api_key,
                            "units": "metric"
                        }
                        response = requests.get(base_url, params=params)
                        data = response.json()
                        if response.status_code == 200:
                            weather_description = data["weather"][0]["description"]
                            temperature = data["main"]["temp"]
                            bot_response = f"The current weather in {location} is {weather_description} with a temperature of {temperature}°C."
                        else:
                            bot_response = "Sorry, I couldn't fetch the weather information."
                    else:
                        bot_response = "Please specify a location for weather information."
                elif 'open youtube' in user_input:
                    # Open YouTube in the default web browser
                    webbrowser.open("https://www.youtube.com")
                    bot_response = "Opening YouTube..."
                else:
                    command = user_input[1:]  # Remove the backslash from the command
                    if command in custom_commands:
                        bot_response = custom_commands[command]
                    else:
                        bot_response = "Unknown command. Type '\\help' for available commands."
            else:
                bot_response = "Unknown command. Type '\\help' for available commands."
        elif user_input in greetings:
            # Get a random response
            bot_response = random.choice(responses)
        elif user_input == 'bye':
            bot_response = "Goodbye!"
            break

