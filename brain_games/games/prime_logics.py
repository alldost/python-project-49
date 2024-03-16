import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_and_check():
    ''' Генерация, вывод и проверка числа '''
    generated_number = random.randint(1, 100)
    question = f'Question: {generated_number}'
    i = generated_number // 2
    while i >= 2:
        if generated_number % i == 0:
            right_answer = 'no'
            return question, right_answer
        i -= 1
    right_answer = 'yes'
    return question, right_answer
