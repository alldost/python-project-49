#!/usr/bin/env python3

from brain_games.scripts.brain_games import greeting
from brain_games.games.games_logics import game_main
from brain_games.cli import welcome_user
from brain_games.games.progression_logics import create_progression


def main():
    greeting()
    text_description = 'What number is missing in the progression?'
    game_main(welcome_user(), text_description, create_progression)


if __name__ == '__main__':
    main()
