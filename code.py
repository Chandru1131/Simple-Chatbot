def chatbot():
    print("Hello, I am your chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif "hello" in user_input.lower():
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a bot, but I'm doing great!")
        else:
            print("Chatbot: I didn't quite understand that.")

# Start the chatbot
chatbot()
