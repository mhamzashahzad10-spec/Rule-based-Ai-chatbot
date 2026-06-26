print("=" * 50)
print("        🤖 Rule-Based AI Chatbot")
print("=" * 50)
print("Hello! I am your AI Assistant.")
print("Type 'help' to see available commands.")
print("Type 'bye' or 'exit' to end the chat.\n")

while True:
    user = input("👤 You: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print("🤖 Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("🤖 Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("🤖 Bot: My name is RuleBot.")

    elif user == "who created you":
        print("🤖 Bot: I was created as a Rule-Based AI Chatbot using Python.")

    elif user == "what is ai":
        print("🤖 Bot: AI stands for Artificial Intelligence.")

    elif user == "what can you do":
        print("🤖 Bot: I can answer simple predefined questions using if-else logic.")

    elif user in ["thank you", "thanks"]:
        print("🤖 Bot: You're welcome! Happy to help.")

    elif user == "help":
        print("\n📋 Available Commands:")
        print("- hi / hello / hey")
        print("- how are you")
        print("- what is your name")
        print("- who created you")
        print("- what is ai")
        print("- what can you do")
        print("- thank you")
        print("- bye / exit\n")

    elif user in ["bye", "exit"]:
        print("🤖 Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("🤖 Bot: Sorry, I don't understand that command. Type 'help' to see available commands.")
