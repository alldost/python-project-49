from brain_games.cli import welcome_user
import prompt


CORRECT_ANSWERS_COUNT = 3


def engine(game_module):
    ''' Основная логика игры с выводом текстовых сообщений'''
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_module.DESCRIPTION)
    i = 0
    while i < CORRECT_ANSWERS_COUNT:
        question, right_answer = game_module.ask_and_check()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
            i += 1
        else:
            wrong_text = 'is wrong answer ;(. Correct answer was'
            print(f"'{user_answer}' {wrong_text} '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
