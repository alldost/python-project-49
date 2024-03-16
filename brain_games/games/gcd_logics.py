import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def ask_and_check():
    ''' Генерация и вывод чисел, определение их НОД '''
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'Question: {first_number} {second_number}'
    gcd = first_number
    while gcd >= 1:
        if first_number % gcd == 0 and second_number % gcd == 0:
            right_answer = gcd
            return question, right_answer
        gcd -= 1
