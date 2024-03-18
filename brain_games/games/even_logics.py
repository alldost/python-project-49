import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    ''' Функция проверки числа на четность '''
    return number % 2 == 0


def ask_and_check():
    ''' Генерация и проверка на чётность случайного числа '''
    generated_number = random.randint(1, 100)
    question = f'Question: {generated_number}'
    if is_even(generated_number) == True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
