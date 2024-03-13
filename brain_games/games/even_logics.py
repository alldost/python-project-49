import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    ''' Генерация числа и определение его чётности '''
    generated_number = random.randint(1, 100)
    print(f'Question: {generated_number}')
    if generated_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
