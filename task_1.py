"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:

    def __init__(self, matrix):
        # Проверка на равенство длин строк матрицы
        for i in range(1, len(matrix)):
            if len(matrix[i]) != len(matrix[0]):
                raise Exception('Строки матрицы разной длины!!!')
        self.shape = [len(matrix), len(matrix[0])]
        self.matrix = matrix

    def __str__(self):
        result_matrix = ''
        for row in self.matrix:
            for el in row:
                result_matrix += f'{el:>5}'
            result_matrix += '\n'
        return result_matrix

    def __add__(self, other):
        assert self.shape == other.shape, 'Размеры матриц не совпадают! Сложение невозможно!!!'
        result_matrix = []
        for i in range(self.shape[0]):
            new_row = []
            for j in range(self.shape[1]):
                new_row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(new_row)
        return Matrix(result_matrix)


while True:
    try:
        m, n = map(int, input('Введите размер матриц через пробел: ').split())
    except ValueError:
        print('Only integers allowed!')
    else:
        break

matrix_1 = Matrix([[randint(0, 100) for _ in range(n)] for _ in range(m)])
matrix_2 = Matrix([[randint(0, 100) for _ in range(n)] for _ in range(m)])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
