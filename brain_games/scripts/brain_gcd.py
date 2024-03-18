#!/usr/bin/env python3

from brain_games.scripts.brain_games import engine
from brain_games.games import gcd_logics


def main():
    engine(gcd_logics)


if __name__ == '__main__':
    main
