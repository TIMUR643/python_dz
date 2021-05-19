from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Ткань на сумму: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5} ткани'

    def abstract(self):
        return 'Smth vary abstract second'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :} ткани'

    def abstract(self):
        pass


coat = Coat(100)
costume = Costume(46)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
