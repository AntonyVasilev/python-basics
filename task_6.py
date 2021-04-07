"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(user_string):
    if user_string.islower():
        result_list = []
        for el in user_string.split():
            if all(list(map(lambda x: 97 <= ord(x) <= 122, el))):
                result_list.append(el.title())
        return ' '.join(result_list)
    else:
        return 'String must include only lowercase characters!'


# print(int_func('nice авп ъghj jапро hjjпаро вапрghgh cool'))
print(int_func(input('Input some words: ')))
