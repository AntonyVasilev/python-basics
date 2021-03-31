"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

num = input('Input an integer number: ')
print(f'{num} + {num + num} + {num + num + num} = {int(num) + int(num + num) + int(num + num + num)}')
