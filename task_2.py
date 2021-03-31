"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_sec = int(input('Input a time in seconds: '))

hours = user_sec // 3600
minutes = (user_sec % 3600) // 60
seconds = user_sec % 60

print(f'{user_sec} seconds equals {hours:>02}:{minutes:>02}:{seconds:>02}.')
