"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going.')

    def stop(self):
        print(f'{self.name} is stopped.')

    def turn(self, direction):
        print(f'{self.name} is turning {direction}.')

    def show_speed(self):
        print(f'Current speed: {self.speed} km/h')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed! Current speed: {self.speed} km/h')
        else:
            print(f'Current speed: {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Over speed! Current speed: {self.speed} km/h')
        else:
            print(f'Current speed: {self.speed} km/h')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(65, 'green', 'Mazda 6')
town_car.show_speed()
town_car.speed = 50
town_car.show_speed()

sport_car = SportCar(80, 'red', 'Ford Mustang')
sport_car.go()
sport_car.turn('left')
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(41, 'white', 'Ford Transit')
work_car.show_speed()
work_car.speed = 40
work_car.show_speed()

police_car = PoliceCar(55, 'white', 'Lada')
print(police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn('right')
police_car.stop()
