"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


try:
    numbers = list(map(int, input('Input two numbers with spaces: ').split()))
    if numbers[1] == 0:
        raise ZeroDivision('На ноль делить нельзя!')
    print(numbers[0] / numbers[1])
except (ValueError, ZeroDivision) as err:
    print(err)
