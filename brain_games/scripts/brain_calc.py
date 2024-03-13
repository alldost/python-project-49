#!/usr/bin/env python3

from brain_games.games.engine import engine
from brain_games.games.calc_logics import DESCRIPTION, expression_generate


def main():
    engine(DESCRIPTION, expression_generate)


if __name__ == '__main__':
    main()
