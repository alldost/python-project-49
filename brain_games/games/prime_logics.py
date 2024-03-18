import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = number // 2
    while i >= 2:
        if number % i == 0:
            return False
        i -= 1
    return True


def ask_and_check():
    ''' Генерация, вывод и проверка числа '''
    generated_number = random.randint(1, 100)
    question = f'Question: {generated_number}'
    if is_prime(generated_number) == True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
