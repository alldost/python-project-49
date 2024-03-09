#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import greeting
from brain_games.games_logics import game_main
from brain_games.cli import welcome_user


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


def main():
    greeting()
    text_description = 'What number is missing in the progression?'
    game_main(welcome_user(), text_description, create_progression)


if __name__ == '__main__':
    main()
