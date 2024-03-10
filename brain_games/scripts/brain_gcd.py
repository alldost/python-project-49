#!/usr/bin/env python3

from brain_games.scripts.brain_games import greeting
from brain_games.games.games_logics import game_main
from brain_games.cli import welcome_user
from brain_games.games.gcd_logics import greatest_gcd


def main():
    greeting()
    text_description = 'Find the greatest common divisor of given numbers.'
    game_main(welcome_user(), text_description, greatest_gcd)


if __name__ == '__main__':
    main
