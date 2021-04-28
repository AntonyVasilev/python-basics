"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В
рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from datetime import datetime

class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def split_data(cls, obj):
        try:
            d, m, y = map(int, obj.data.split('-'))
        except ValueError:
            print('Было введено не число!')
        else:
            if cls.validate_data(d, m, y):
                return d, m, y

    @staticmethod
    def validate_data(d, m, y):
        try:
            datetime.strptime(f'{d}.{m}.{y}', '%d.%m.%Y')
        except ValueError:
            print('Введенные данные не являются датой!')
        else:
            return True


new_data = Data('24-06-2021')
try:
    day, month, year = Data.split_data(new_data)
except TypeError as err:
    pass
else:
    print(day, month, year)
    print(type(day), type(month), type(year))
