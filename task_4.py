"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
# Предварительно необходимо установить модуль: pip install translate

from translate import Translator

translator = Translator(to_lang='Russian')

# Использую файл из архива
with open('text_4_result.txt', 'w', encoding='utf-8') as f_res:
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        for row in f:
            f_res.write(f"{translator.translate(row.split(' - ')[0])} - {row.split(' - ')[1]}")


# Вариант перевода через словарь. При таком объеме данных работает намного быстрее, чем модуль translate.

# translations = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#
# with open('text_4_result.txt', 'w', encoding='utf-8') as f_res:
#     with open('text_4.txt', 'r', encoding='utf-8') as f:
#         for row in f:
#             f_res.writelines(f"{translations[row.split(' - ')[0]]} - {row.split(' - ')[1]}")
