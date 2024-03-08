#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.even_logics import greeting, even_game


def main():
    greeting()
    even_game(welcome_user())


if __name__ == '__main__':
    main()
