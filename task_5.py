"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [8, 6, 5, 3, 2, 2, 2]
while True:
    print(my_list)
    new_num = int(input('Input a new number or 0 to quit: '))
    if new_num == 0:
        break
    elif new_num > 0:
        for i, num in enumerate(my_list):
            if new_num > num:
                my_list.insert(i, new_num)
                break
        else:
            my_list.append(new_num)
    else:
        print('Wrong input! A new number must be positive.')
