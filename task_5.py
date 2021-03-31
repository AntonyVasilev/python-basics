"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

income = float(input('Input a company income: '))
costs = float(input('Input a company costs: '))
profit = income - costs

if profit > 0:
    print(f'The company made a profit.')
    profitability = profit / income
    num_employees = int(input('Input employees number: '))
    profit_per_employee = profit / num_employees
    print(f'Profitability = {profitability:.2f}, profit per an employee = {profit_per_employee:.2f}')
elif profit < 0:
    print('The company suffered a loss.')
else:
    print('The company received zero profit.')
