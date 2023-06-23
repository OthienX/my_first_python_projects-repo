import random

# Define a list of greetings and corresponding responses
greetings = ['hello', 'hi', 'hey', 'greetings']
responses = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']

# Define a function to generate a random response
def get_random_response(responses):
    return random.choice(responses)

# Main loop to handle user input
while True:
    # Get user input
    user_input = input("User: ")

    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if user input is a command
    if user_input.startswith('\\'):
        # Process different commands
        if user_input == '\\help':
            print("Bot: I am just a simple bot created with Python.")
        elif user_input == '\\info':
            print("Bot: I wish I could help you with what you need.")
        else:
            print("Bot: Unknown command. Type '\\help' for available commands.")
    elif user_input in greetings:
        # Get a random response and print it
        response = get_random_response(responses)
        print("Bot:", response)
    elif user_input == 'bye':
        # Exit the loop if the user says 'bye'
        print("Bot: Goodbye!")
        break
    else:
        # If user input doesn't match any predefined patterns or commands, provide a default response
        print("Bot: I'm sorry, I didn't understand that.")
