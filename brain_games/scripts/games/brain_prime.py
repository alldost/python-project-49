#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import greeting
from brain_games.games_logics import game_main
from brain_games.cli import welcome_user


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


def main():
    greeting()
    text_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_main(welcome_user(), text_description, is_prime)


if __name__ == '__main__':
    main()
