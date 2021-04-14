"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""

with open('text_3.txt', 'r', encoding='utf-8') as f:
    salaries = {row.split()[0]: float(row.split()[1]) for row in f}

print(f'Mean salary is {sum(salaries.values()) / len(salaries)}')
print(f'Employees with salary below 20000: {[surname for surname, salary in salaries.items() if salary < 20000]}')
