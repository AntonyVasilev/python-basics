"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

try:
    with open('user_data.txt', 'w', encoding='utf-8') as f:
        user_input = True
        while user_input:
            user_input = input('Input some data to write to the file or nothing to stop: ')
            if user_input:
                f.write(f'{user_input}\n')
except IOError as err:
    print(err)
