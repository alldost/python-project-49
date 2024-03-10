import random


def create_progression():
    ''' Создает и выводит прогрессию, заменяя случайный элемент на .. '''
    progression_length = random.randint(5, 10)
    step = random.randint(1, 10)
    first_element = random.randint(1, 50)
    last_element = first_element + step * progression_length + 1
    progression = list(range(first_element, last_element, step))
    replaced_index = random.randint(0, progression_length)
    replaced_value = progression[replaced_index]
    progression[replaced_index] = '..'
    print('Question: ', *progression)
    return replaced_value
