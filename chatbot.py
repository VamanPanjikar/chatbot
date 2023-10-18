import nltk
import sys
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chat bot
chatbot_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I'm just a chat bot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|great|fine|well)",
        ["That's great to hear!",]
    ],
    [
        r"(bye|goodbye|exit)",
        ["Goodbye! Have a nice day.", "Chat bot has exited."]
    ],
    [
        r"Can i ask you personal questions?",
        ["Im sorry, As an AI chatbot i cannot answer them.",]
    ],
    [
        r"hi",
        ["hello",]
    ],
]

# Create and set up the chat bot
def chatbot():
    print("Hello! I'm a chat bot.")
    chat = Chat(chatbot_pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
    sys.exit()
