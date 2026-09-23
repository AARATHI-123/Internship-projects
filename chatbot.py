import datetime
import random

# -----------------------------
# Chatbot memory
# -----------------------------

user_name = None
conversation_history = []


# -----------------------------
# Chatbot response function
# -----------------------------

def chatbot_response(message):
    global user_name

    original_message = message
    message = message.lower().strip()

    # Save conversation
    conversation_history.append(("You", original_message))

    # Greetings
    if message in ["hello", "hi", "hey", "good morning", "good evening"]:
        responses = [
            "Hello! 😊",
            "Hi there! How can I help?",
            "Hey! Nice to talk to you!"
        ]
        response = random.choice(responses)

    # How are you
    elif message in ["how are you", "how are you doing"]:
        response = "I'm doing great! 🤖 How about you?"

    # User says they are fine
    elif message in ["i am fine", "i'm fine", "fine", "good"]:
        response = "That's great to hear! 😊"

    # Name
    elif message.startswith("my name is "):
        user_name = message[11:].strip().title()
        response = f"Nice to meet you, {user_name}! 😊"

    # Recall name
    elif message in ["what is my name", "do you know my name"]:
        if user_name:
            response = f"Your name is {user_name}."
        else:
            response = "I don't know your name yet."

    # Time
    elif message == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."

    # Date
    elif message == "date":
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        response = f"Today is {current_date}."

    # Day
    elif message == "day":
        today = datetime.datetime.now().strftime("%A")
        response = f"Today is {today}."

    # Jokes
    elif message == "joke":
        jokes = [
            "Why did the computer go to the doctor? Because it had a virus! 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the computer cold? Because it left its Windows open! 😂",
            "What do you call a computer that sings? A Dell! 🎵"
        ]
        response = random.choice(jokes)

    # Calculator
    elif message.startswith("calculate "):
        expression = message[10:]

        try:
            result = eval(expression)
            response = f"The answer is {result}."
        except:
            response = "I couldn't calculate that. Try something like: calculate 20 + 5"

    # Yes / No
    elif message in ["yes", "yeah", "yep"]:
        response = "Awesome! 👍"

    elif message in ["no", "nope"]:
        response = "Okay! 😊"

    # Conversation history
    elif message in ["history", "show history"]:
        if len(conversation_history) <= 1:
            response = "We haven't talked much yet!"
        else:
            history = ""

            for speaker, text in conversation_history[:-1]:
                history += f"{speaker}: {text}\n"

            response = "Here's our conversation:\n" + history

    # Help
    elif message == "help":
        response = """
🤖 Commands you can use:

hello
how are you
my name is John
what is my name
time
date
day
joke
calculate 10 + 5
history
help
bye
"""

    # Goodbye
    elif message == "bye":
        response = "Goodbye! It was nice talking to you! 👋"

    # Unknown input
    else:
        response = (
            "I'm not sure how to respond to that. 🤔\n"
            "Type 'help' to see what I can do."
        )

    # Save bot response
    conversation_history.append(("Bot", response))

    return response


# -----------------------------
# Start chatbot
# -----------------------------

print("=" * 40)
print("🤖 ADVANCED PYTHON CHATBOT")
print("=" * 40)

print("Hello! I'm your chatbot.")
print("Type 'help' to see my commands.")
print("Type 'bye' to exit.")

# -----------------------------
# Main loop
# -----------------------------

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower().strip() == "bye":
        break