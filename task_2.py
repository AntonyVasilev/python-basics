"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
from random import randint, randrange

el_num = randrange(5, 20)
my_list = [randint(-100, 100) for _ in range(el_num)]
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(f'Initial list:\t{my_list}')
print(f'Result list:\t{result_list}')
