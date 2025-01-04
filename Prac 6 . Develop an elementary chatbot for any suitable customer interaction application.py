import random

# Define a dictionary of predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm just a chatbot, but thanks for asking!", "I don't have feelings, but I'm here to assist you."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "weather": ["The weather is sunny today.", "I'm sorry, I don't have access to real-time weather data."],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?", "I didn't understand that."],
}

# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check if the user input matches predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no predefined response is found, return a default response
    return random.choice(responses["default"])

# Main chat loop
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
