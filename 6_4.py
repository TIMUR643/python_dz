class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет.'

    def stop(self):
        return f'{self.name} стоит.'

    def turn(self, direction):
        return f' {self.name} повернул на  {direction}'

    def show_speed(self):
        return f'Ваша скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Сбавьте скорость'
        else:
            return f'Скорость {self.name}  разрешенная'

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Сбавьте скорость'
        else:
            return f'Скоость {self.name} разрешенная'


class PoliceCar(Car):
    pass


town = TownCar('Nissan', 100, 'красный', False)
print(town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('Lambo', 220, ';желтый', False)
print( sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop())

work = WorkCar('lada', 30, 'фиолетовый', False)
print( work.go(), work.show_speed(), work.turn('право'), work.stop())

police = PoliceCar('BMW', 100, 'черный', True)
print( police.go(), police.show_speed(), police.turn('право'), police.stop())
