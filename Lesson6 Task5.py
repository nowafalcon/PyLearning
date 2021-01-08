# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Тут могла быть Ваша реклама')


class Pen(Stationery):

    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'Используем: {self.title}')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'Используем: {self.title}')


class Handle(Stationery):

    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'Используем: {self.title}')


if __name__ == '__main__':
    p = Pen()
    n = Pencil()
    h = Handle()
    s = Stationery('Канцелярская принадлежность')

    p.draw()
    n.draw()
    h.draw()
    s.draw()
