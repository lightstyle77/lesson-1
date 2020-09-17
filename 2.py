# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes:
    v = 0
    h = 0

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    @property
    def calculation(self):
        return self.v / 6.5 + 0.5

    def __add__(self, other):
        return self.calculation + other.calculation


class Jacket(Clothes):

    @property
    def calculation(self):
        return 2 * self.h + 0.3

    def __add__(self, other):
        return self.calculation + other.calculation


coat_class = Coat(54, 170)
jacket_class = Jacket(50, 186)
print(jacket_class.calculation)
print(coat_class.calculation)
print(jacket_class + coat_class)
