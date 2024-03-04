#!/usr/bin/env python3

from ..cli import welcome_user
from ..even_logics import greeting, question_content, is_answer_correct


def even_game(name):
    ''' Основная логика игры с выводом текстовых сообщений'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        if is_answer_correct(question_content()) == 1:
            i += 1
        else:
            print(f"Let's try again, {name}!")
            i = 1
    print(f'Congratulations, {name}!')


def main():
    greeting()
    even_game(welcome_user())


if __name__ == '__main__':
    main()
