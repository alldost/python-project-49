import random
import prompt


def greeting():
    print('Welcome to the Brain Games!')


def question_content():
    ''' Генерация случайного числа и вывод вопроса '''
    generated_number = random.randint(1, 100)
    print(f'Question: {generated_number}')
    return generated_number


def is_answer_correct(generated_number):
    ''' Получение ответа от пользователя и оценка его корректности '''
    user_answer = prompt.string('Your answer: ')
    if generated_number % 2 == 0:
        if user_answer == 'yes':
            print('Correct!')
            return 1
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return 0
    else:
        if user_answer == 'no':
            print('Correct!')
            return 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return 0
