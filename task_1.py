"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def numbers_division(x, y):
    try:
        result = round(x / y, 4)
    except ZeroDivisionError as exc:
        return exc
    else:
        return result


print(numbers_division(int(input('Input the first number: ')), int(input('Input the second number: '))))
