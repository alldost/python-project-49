import random


def expression_generate():
    ''' Генерирует и выводит на экран случайное математическое выражение '''
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.randint(1, 3)
    match operator:
        case 1:
            result = first_number + second_number
            print(f"Question: {first_number} + {second_number}")
        case 2:
            result = first_number - second_number
            print(f"Question: {first_number} - {second_number}")
        case 3:
            result = first_number * second_number
            print(f"Question: {first_number} * {second_number}")
    return result
