import time
now = time.ctime()
qna = {
    "hi":"hey",
    "how are you":"I am fine",
    "what is your name ":"my name is chatbot2.o",
    "who are you?": "I am basic text_based chatbot.",
    "how old are you?":"I am 1 year old.",
    "tell me about yourself?": "I am basic text_based chatbot.",
    "what is the time now":now,


}
while True:
    question= input("You: ")
    if(question== "quit"):
        break

    else:
        print("Bot:",qna[question])
