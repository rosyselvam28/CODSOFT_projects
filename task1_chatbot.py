# CODSOFT AI Internship
# Task 1 - Chatbot with Rule-Based Responses

import datetime


def display_header():
    print("\n" + "=" * 50)
    print("          AI CHATBOT ASSISTANT")
    print("=" * 50)


def display_options():
    print("\nYou can ask questions like:")

    questions = [
        "hello",
        "how are you",
        "your name",
        "what is python",
        "what is artificial intelligence",
        "who created python",
        "date",
        "time",
        "internship",
        "help",
        "bye"
    ]

    for item in questions:
        print("•", item)


def get_response(user):

    user = user.strip().lower()

    if user in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"

    elif user == "how are you":
        return "I am doing well. Thank you for asking."

    elif user in ["your name", "what is your name"]:
        return "I am a rule-based AI chatbot developed using Python."

    elif user == "what is python":
        return "Python is a popular high-level programming language used in AI, web development and data science."

    elif user == "what is artificial intelligence":
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."

    elif user == "who created python":
        return "Python was created by Guido van Rossum in 1991."

    elif user == "date":
        today = datetime.date.today()
        return f"Today's date is {today}"

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif user == "internship":
        return "Internships help students gain practical knowledge and improve their technical skills."

    elif user == "help":
        return "Please choose one of the available questions shown above."

    elif user == "bye":
        return "Goodbye! Thank you for using the chatbot."

    else:
        return "Sorry, I don't understand that question."


def chatbot():

    display_header()

    print("Welcome to the AI Chatbot.")
    print("Type 'bye' to exit.")

    while True:

        display_options()

        user_input = input("\nYou : ")

        response = get_response(user_input)

        print("\nBot :", response)

        if user_input.strip().lower() == "bye":
            break


chatbot()