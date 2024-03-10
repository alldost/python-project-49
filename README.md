### Hexlet tests and linter status:
[![Actions Status](https://github.com/alldost/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alldost/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/38b2e975660c21c973a6/maintainability)](https://codeclimate.com/github/alldost/python-project-49/maintainability)


Проект "Игры разума" содержит 5 консольных игр:

- "Проверка на четность" (brain-even)
- "Калькулятор" (brain-calc)
- "НОД" (brain-gcd)
- "Арифметическая прогрессия" (brain-progression)
- "Простое ли число?" (brain-prime) 

Для победы в каждой игре необходимо дать три правильных ответа подряд. В случае выбора неправильного ответа
прогресс сбрасывается, и на экран выводится правильный ответ. 


Минимальные требования для запуска проекта:

- Python версии 3.6 или выше
- Pip версии 19 или выше
- Poetry версии 1.2.0 или выше (для установки можно воспользоваться командой make install)


Для установки пакета необходимо выполнить следующие команды:

1) Выполнить сборку командой make build (альтернативна - poetry build )
2) Выполнить публикацию командой make publish (альтернатива - poetry publish --dry-run)
3) Выполнить установку пакета командой make package-install (альтернатива - python3 -m pip install --user dist/*.whl)
4) !Опционально! В случае, если пакет уже был установление, но в него были внесены изменеиня, следует 
переустановить пакет командой make package-reinstall 
(альтернатива - python3 -m pip install --user --force-reinstall dist/*.whl)


Для запуска игр необходимо использовать команды, указанные выше рядом с названиями (ex: brain-even)

Примеры установки пакета и запуска конкретных игр:

1. "Проверка на четность":

[brain-even](https://asciinema.org/a/GUX57w2exnhHn3IwucJa1HtoE)

2. "Калькулятор":

[brain-calc](https://asciinema.org/a/4Yd587oZw9oYQdA6WKyrnzlTI)

3. "НОД"

[brain-gcd](https://asciinema.org/a/uQGcIzjq0bEcmSYsb3njppWvT)

4. "Арифметическая прогрессия":

[brain-progression](https://asciinema.org/a/6fZPR1C77M22u9JoAN99UunB0)

5. "Простое ли число?":

[brain-prime](https://asciinema.org/a/O3MGcse9ba2Zv5ITkhUd14mMC)
