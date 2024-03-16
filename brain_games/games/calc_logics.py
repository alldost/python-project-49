import random


DESCRIPTION = 'What is the result of the expression?'


def ask_and_check():
    ''' Генерирует случайное математическое выражение и вычисляет результат'''
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.randint(1, 3)
    match operator:
        case 1:
            question = f"Question: {first_number} + {second_number}"
            right_answer = first_number + second_number
        case 2:
            question = f"Question: {first_number} - {second_number}"
            right_answer = first_number - second_number
        case 3:
            question = f"Question: {first_number} * {second_number}"
            right_answer = first_number * second_number
    return question, right_answer
