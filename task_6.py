"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат
спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
"""

a = float(input('Input result at the first day in kilometers: '))
b = float(input('Input target result in kilometers: '))
n = 1

while a < b:
    a *= 1.1
    n += 1

print(f'The sportsman achieved the result of {b} kilometers or more on the {n}th day.')
