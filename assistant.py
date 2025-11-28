def system_prompt():
    return "You are a friendly study assistant. Keep answers short and helpful."

def respond(user_message):
    # Simulated assistant logic (no AI needed)
    if "help" in user_message.lower():
        return "Sure! Tell me what topic you want help with."
    elif "python" in user_message.lower():
        return "Python is a simple and powerful programming language."
    elif "ml" in user_message.lower():
        return "Machine Learning helps computers learn from data."
    else:
        return "I can help with study topics like Python, ML, AI. Ask me anything!"

# Simple loop (simulated dialogue)
if _name_ == "_main_":
    print("Assistant: Hello! How can I help you today? (type 'exit' to stop)")

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Assistant: Goodbye! 👋")
            break
        reply = respond(user)
        print("Assistant:", reply)
