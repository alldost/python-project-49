#!/usr/bin/env python3

from brain_games.games.engine import engine
from brain_games.games.even_logics import DESCRIPTION, is_even


def main():
    engine(DESCRIPTION, is_even)


if __name__ == '__main__':
    main()
