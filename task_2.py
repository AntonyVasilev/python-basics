"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def print_user_info(*, name, surname, year, city, email, phone_number):
    print(f'User: {name} {surname}, year of birth: {year}, from {city}, email: {email}, phone number: {phone_number}.')


print_user_info(name='John', surname='White', city='New York', email='john_white@gmail.com', year='1955',
                phone_number='+15555555555')

print_user_info(phone_number='+7800000000', name='Ivan', surname='Ivanov', city='Moscow', email='ii@mail.ru', year=1990)
