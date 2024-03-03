import prompt


def welcome_user():
	'''Получение имени пользователя и его приветствие'''
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
