import prompt


def is_answer_correct(right_answer):
    ''' Получение ответа от пользователя и оценка его корректности '''
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(right_answer):
        print('Correct!')
        return 1
    else:
        wrong_text = 'is wrong answer ;(. Correct answer was'
        print(f"'{user_answer}' {wrong_text} '{right_answer}'.")
        return 0


def game_main(name, text_description, right_answer):
    ''' Основная логика игры с выводом текстовых сообщений'''
    print(text_description)
    i = 1
    while i <= 3:
        if is_answer_correct(right_answer()) == 1:
            i += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
