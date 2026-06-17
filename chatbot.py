faq = {
    "what is python": "Python is a programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning helps computers learn from data.",
    "what is data science": "Data Science extracts insights from data.",
    "who are you": "I am a FAQ Chatbot.",
    "what is codealpha": "CodeAlpha provides internship programs.",
    "how are you": "I am fine.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is chatbot": "A chatbot is a program that answers questions.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning."
}

print("FAQ Chatbot Started!")
print("Type 'exit' to quit.")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    if user in faq:
        print("Bot:", faq[user])
    else:
        print("Bot: Sorry, I don't know the answer.")