"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def sum_numbers():
    result, current_sum = 0, 0
    while True:
        new_nums = input('Input numbers with spaces: ').split()
        if 'q' in new_nums:
            new_nums.remove('q')
            result += sum(map(float, new_nums))
            return result
        else:
            current_sum = sum(map(float, new_nums))
            result += current_sum
            print(f'Current sum is {current_sum}, result sum is {result}')


print(sum_numbers())
