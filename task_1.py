"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
"""

# Калькулятор

x = float(input('Input the first number: '))
op = input('Input +, -, *, **, /, //, %: ')
y = float(input('Input the second number: '))

if op == '+':
    print(f'{x} {op} {y} = {x + y}')
elif op == '-':
    print(f'{x} {op} {y} = {x - y}')
elif op == '*':
    print(f'{x} {op} {y} = {x * y}')
elif op == '**':
    print(f'{x} {op} {y} = {x ** y}')
elif op == '/':
    print(f'{x} {op} {y} = {x / y}')
elif op == '//':
    print(f'{x} {op} {y} = {x // y}')
elif op == '%':
    print(f'{x} {op} {y} = {x % y}')
else:
    print('Wrong input!')
