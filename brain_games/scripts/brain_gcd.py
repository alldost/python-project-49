#!/usr/bin/env python3

from brain_games.games.engine import engine
from brain_games.games.gcd_logics import DESCRIPTION, greatest_gcd


def main():
    engine(DESCRIPTION, greatest_gcd)


if __name__ == '__main__':
    main
