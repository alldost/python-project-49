import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def ask_and_check():
    ''' Генерация и вывод чисел, определение их НОД '''
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'Question: {first_number} {second_number}'
    right_answer = math.gcd(first_number, second_number)
    return question, right_answer
