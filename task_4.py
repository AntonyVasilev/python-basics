"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = int(input('Input a positive integer number: '))
max_digit = 0

while num:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10

print(f'Max digit is {max_digit}')
