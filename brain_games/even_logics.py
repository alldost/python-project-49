import random
import prompt


def greeting():
    print('Welcome to the Brain Games!')


def question_content():
    ''' Генерация случайного числа и вывод вопроса '''
    generated_number = random.randint(1, 100)
    print(f'Question: {generated_number}')
    return generated_number


def right_answer(generated_number):
    ''' Функция определения чётности числа '''
    if generated_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def is_answer_correct(right_answer):
    ''' Получение ответа от пользователя и оценка его корректности '''
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
        return 0


def even_game(name):
    ''' Основная логика игры с выводом текстовых сообщений'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        if is_answer_correct(right_answer(question_content())) == 1:
            i += 1
        else:
            print(f"Let's try again, {name}!")
            i = 1
    print(f'Congratulations, {name}!')
