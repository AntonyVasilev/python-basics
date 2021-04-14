"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    companies = {row.split()[0]: float(row.split()[2]) - float(row.split()[3]) for row in f}

profit_list = [value for value in companies.values() if value > 0]

result_list = [companies, {'average_profit': sum(profit_list) / len(profit_list)}]

print(result_list)

with open('text_7.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, sort_keys=True, indent=4, ensure_ascii=False)
