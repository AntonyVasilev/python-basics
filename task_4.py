"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_1(x, y):
    if x > 0 and y < 0 and str(abs(y)).isdigit():
        result = 1
        for i in range(abs(y)):
            result *= x
        return round(1/result, 4)
    else:
        return 'Wrong arguments. X must be positive and Y must be negative & integer!'


def my_func_2(x, y):
    if x > 0 and y < 0 and str(abs(y)).isdigit():
        return x ** y
    else:
        return 'Wrong arguments. X must be positive and Y must be negative & integer!'


number = float(input('Input a number: '))
degree = int(input('Input negative degree: '))
print(my_func_1(number, degree))
print(my_func_2(number, degree))
