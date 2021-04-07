"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(*args):
    numbers_list = list(args)
    numbers_list.remove(min(numbers_list))
    return round(sum(numbers_list), 4)


print(my_func(*list(map(float, input('Input three numbers with spaces: ').split()))))
