from brain_games.scripts.brain_games import greeting
from brain_games.games.games_logics import game_main
from brain_games.cli import welcome_user


def engine(DESCRIPTION, game_module):
    greeting()
    game_main(welcome_user(), DESCRIPTION, game_module)
