def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. How can I help you today?")
    
    while True:
        # Get user input
        user_input = input("You: ").lower()
        
        # Define rules for responses
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase?")
            
# Run the chatbot
chatbot()
