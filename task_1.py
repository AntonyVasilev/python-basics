"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    path, hours, rate, bonus = argv
except ValueError:
    print('You should input number of hours, rate of payment per hour and month bonus as parameters after script name.')
else:
    try:
        print(f'Your salary is {float(hours) * float(rate) + float(bonus):.2f} rubles.')
    except ValueError as msg:
        print('Your salary did not count,', msg)
