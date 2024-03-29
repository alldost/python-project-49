import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    else:
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
    right_answer = 'yes' if is_prime(generated_number) is True else 'no'
    return question, right_answer
