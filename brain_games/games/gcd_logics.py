import random


def greatest_gcd():
    ''' Генерация и вывод чисел, определение их НОД '''
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(f'Question: {first_number}  {second_number}')
    gcd = first_number
    while gcd >= 1:
        if first_number % gcd == 0 and second_number % gcd == 0:
            return gcd
        gcd -= 1
