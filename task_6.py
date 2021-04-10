"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle, repeat


def nums_iterator(start_num, num_iterations):
    i = 0
    for el in count(start_num):
        if i < num_iterations:
            yield el
            i += 1
        else:
            return el


def elements_repeater(repeat_list, num_iterations):
    i = 0
    for el in cycle(repeat_list):
        if i < num_iterations:
            yield el
            i += 1
        else:
            return el


for num in nums_iterator(5, 7):
    print(num)

print('\n', '*' * 20, '\n')

for char in elements_repeater('python', 10):
    print(char)
