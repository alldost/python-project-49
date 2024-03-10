#!/usr/bin/env python3

from brain_games.scripts.brain_games import greeting
from brain_games.games.games_logics import game_main
from brain_games.cli import welcome_user
from brain_games.games.calc_logics import expression_generate


def main():
    greeting()
    text_description = 'What is the result of the expression?'
    game_main(welcome_user(), text_description, expression_generate)


if __name__ == '__main__':
    main()
