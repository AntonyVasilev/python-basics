"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

from re import findall


class ComplexNumbers:

    def __init__(self, complex_number):
        self.complex_number = complex_number

    @staticmethod
    def split_number(number):
        num = findall(r'[1-9]+', number)
        # Если мнимое число равно 1 и записано как i, добавляю 1 в список
        if len(num) == 1:
            num.append('1')
        # Добавляю знак "-" если он стоит перед мнимым числом
        if '-' in number[1:]:
            num[1] = f'-{num[1]}'
        try:
            x, y = map(int, num)
        except ValueError:
            print('Only integer numbers allowed!')
        else:
            return x, y

    def __str__(self):
        return self.complex_number

    def __add__(self, other):
        a, b = self.split_number(self.complex_number)
        c, d = self.split_number(other.complex_number)
        x = a + c
        y = b + d
        return ComplexNumbers(f'{x}+{y}i') if y >= 0 else ComplexNumbers(f'{x}{y}i')

    def __mul__(self, other):
        a, b = self.split_number(self.complex_number)
        c, d = self.split_number(other.complex_number)
        x = a * c - b * d
        y = a * d + c * b
        return ComplexNumbers(f'{x}+{y}i') if y >= 0 else ComplexNumbers(f'{x}{y}i')


c_num_1 = ComplexNumbers('3+i')
c_num_2 = ComplexNumbers('2+3i')
print(c_num_1 + c_num_2)
print(c_num_1 * c_num_2)
