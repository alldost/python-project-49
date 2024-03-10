import random


def is_prime():
    ''' Генерация, вывод и проверка числа '''
    generated_number = random.randint(1, 100)
    print(f'Question: {generated_number}')
    i = generated_number // 2
    while i >= 2:
        if generated_number % i == 0:
            return 'no'
        i -= 1
    return 'yes'
