# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это
# могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
# костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
class Odezhda:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def total(self):
        return self.a.square() + self.b.square()

    def __str__(self):
        return f'Площадь ткани общая:\n{round(self.total(), 2)}'


class Jacket:
    def __init__(self, a):
        self.a = a

    def square(self):
        return self.a / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто:\n{round(self.square(),2)}'


class Coat:
    def __init__(self, a):
        self.a = a

    def square(self):
        return self.value * 2 + 0.3

    # Просто воткнул property, чтоб было
    @property
    def value(self):
        return self.a

    def __str__(self):
        return f'Площадь на пальто:\n{round(self.square(),2)}'


coat = Coat(8)
jacket = Jacket(4)
total = Odezhda(jacket, coat)
print(coat)
print(jacket)
print(total)
