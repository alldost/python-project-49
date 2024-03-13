#!/usr/bin/env python3

from brain_games.games.engine import engine
from brain_games.games.prime_logics import DESCRIPTION, is_prime


def main():
    engine(DESCRIPTION, is_prime)


if __name__ == '__main__':
    main()
