#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import greeting
from brain_games.games_logics import game_main
from brain_games.cli import welcome_user


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


def main():
    greeting()
    text_description = 'Find the greatest common divisor of given numbers.'
    game_main(welcome_user(), text_description, greatest_gcd)


if __name__ == '__main__':
    main
