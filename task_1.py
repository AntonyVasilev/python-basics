"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __color = [['red', '\033[31m', 7], ['yellow', '\033[33m', 2], ['green', '\033[32m', 5]]

    def running(self, n_loops):
        i = 1
        colour = 0
        direction = 1
        while i <= n_loops:
            print(f'{self.__color[colour][1]}{self.__color[colour][0]}')
            sleep(self.__color[colour][2])
            colour += direction
            i += 1
            if colour == 0 or colour == 2:
                direction *= -1


lights = TrafficLight()
lights.running(10)


