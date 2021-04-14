"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join([str(randint(-100, 100)) for _ in range(randint(5, 20))]))

with open('numbers.txt', 'r', encoding='utf-8') as f:
    num_list = list(map(int, f.read().split()))

print(f'The sum of the numbers equals {sum(num_list)}')
