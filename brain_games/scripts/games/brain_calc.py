#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import greeting
from brain_games.games_logics import game_main
from brain_games.cli import welcome_user


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


def main():
    greeting()
    text_description = 'What is the result of the expression?'
    game_main(welcome_user(), text_description, expression_generate)


if __name__ == '__main__':
    main()
