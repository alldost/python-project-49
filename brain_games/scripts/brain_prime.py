#!/usr/bin/env python3

from brain_games.scripts.brain_games import greeting
from brain_games.games.games_logics import game_main
from brain_games.cli import welcome_user
from brain_games.games.prime_logics import is_prime


def main():
    greeting()
    text_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_main(welcome_user(), text_description, is_prime)


if __name__ == '__main__':
    main()
