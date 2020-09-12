# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print(f'Рисует {Pen.title}')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print(f'Рисует {Pencil.title}')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print(f'Рисует {Handle.title}')


Pen = Pen()
Pen.draw()
Pencil = Pencil()
Pencil.draw()
Handle = Handle()
Handle.draw()
