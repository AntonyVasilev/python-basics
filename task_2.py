"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import abstractmethod


class Clothes:

    @abstractmethod
    def cloth_count(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def cloth_count(self):
        return round(self.v / 6.5 + 0.5, 3)


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    def cloth_count(self):
        return round(2 * self.h + 0.3, 3)

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 0:
            self.__h = 0
        else:
            self.__h = h


coat = Coat(39)
print(coat.cloth_count)

suit = Suit(1.8)
print(suit.cloth_count())

suit_2 = Suit(-1)
print(suit_2.cloth_count())
