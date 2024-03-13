#!/usr/bin/env python3

from brain_games.games.engine import engine
from brain_games.games.progression_logics import DESCRIPTION, create_progression


def main():
    engine(DESCRIPTION, create_progression)


if __name__ == '__main__':
    main()
