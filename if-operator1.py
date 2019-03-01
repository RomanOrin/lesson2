age1 = input('Please, write your age: ')


def age_determinator(age):
    age = abs(int(age))
    if age < 3:
        my_answer = 'You are only baby!'
    elif age <7:
        my_answer = 'You should be in a kindergarden'
    elif age <=17:
        my_answer = 'You are student - study a lot!'
    elif age <=22:
        my_answer = 'Work and study! - only these words you should know during the unversity years'
    elif age >=23:
        my_answer = 'Go to get Masters degree or search for work'
    return my_answer
    
print(age_determinator(age1))