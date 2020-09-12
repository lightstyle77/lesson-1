# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат

class Car:
    speed = 0
    color = 'black'
    name = 'Bumblebee'
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def show_attributes(self):
        print(f'Атрибуты: speed = {self.speed}, color = {self.color}, name = {self.name}, is_police = {self.is_police}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Едем на городской машине. Скорость превышена на {self.speed - 60}')
        else:
            print(f'Едем на городской машине. Текущая скорость {self.speed}')


class SportCar(Car):
    is_police = False

    def show_speed(self):
        print(f'Едем на спортивной машине. Текущая скорость {self.speed}')


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Едем на рабочей машине. Скорость превышена на {self.speed - 40}')
        else:
            print(f'Едем на рабочей машине. Текущая скорость {self.speed}')


class PoliceCar(Car):
    is_police = True

    def show_speed(self):
        print(f'Едем на полицейской машине. Текущая скорость {self.speed}')


WorkCar = WorkCar(90, 'Green', 'KamaZ')
TownCar = TownCar(100, 'Red', 'Volga')
SportCar = SportCar(300, 'Orange', 'Mustang')
PoliceCar = PoliceCar(50, 'Blue', 'Vesta')
WorkCar.go()
WorkCar.show_speed()
WorkCar.turn('налево')
WorkCar.stop()
TownCar.go()
TownCar.show_speed()
TownCar.turn('направо')
TownCar.stop()
SportCar.go()
SportCar.show_speed()
SportCar.turn('наискосок направо')
SportCar.stop()
PoliceCar.go()
PoliceCar.show_speed()
PoliceCar.turn('наискосок налево')
PoliceCar.stop()
WorkCar.show_attributes()
TownCar.show_attributes()
SportCar.show_attributes()
PoliceCar.show_attributes()

