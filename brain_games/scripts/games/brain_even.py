#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import greeting
from brain_games.games_logics import game_main
from brain_games.cli import welcome_user


def number_generate():
    ''' Генерация числа и определение его чётности '''
    generated_number = random.randint(1, 100)
    print(f'Question: {generated_number}')
    if generated_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    greeting()
    text_description = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_main(welcome_user(), text_description, number_generate)


if __name__ == '__main__':
    main()
