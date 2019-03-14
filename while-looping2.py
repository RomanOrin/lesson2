answers = {
    "How are you?": "Good",
    "What are you doing?": "Programming"
}

def get_answer(question, answer):
    return answers.get(question)
    
def ask_user(answers):
    while True:
        try:
            user_say = input("Say something: ")
            answer = get_answer(user_say, answers)
            print(answer)
            
        except KeyboardInterrupt:
            print(" It is so sad that you are leaving us!")
            break

ask_user(answers)