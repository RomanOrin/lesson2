answers = {
    "How are you?": "Good",
    "What are you doing?": "Programming"
}

def get_answer(question, answer):
    return answers.get(question)

def ask_user(answers):
    while True:
        user_input = input("Say something: ")
        answer = get_answer(user_input, answers)
        print(answer)

        if user_input == 'Goodbye':
            print('Bye!')
            break
ask_user(answers)