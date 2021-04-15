"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

# Использую файл, созданный в 1 задании
with open('user_data.txt', 'r', encoding='utf-8') as f:
    for i, row in enumerate(f, 1):
        print(f'Row {i} has {len(row.split())} words.')
    print(f'Total number of rows is {i}')
