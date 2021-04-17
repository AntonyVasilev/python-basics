"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
(доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]:.2f} руб.'


new_worker = Position('Ivan', 'Ivanov', 'programmer', 150000, 50000)
print(new_worker.name, new_worker.surname, new_worker.position, new_worker._income)

print(new_worker.get_full_name())
print(new_worker.get_total_income())

