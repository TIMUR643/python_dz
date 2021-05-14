class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print('Запуск отрисовки')
        return self.title

class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print('Запуск отрисовки')
        return self.title

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print('Запуск отрисовки')
        return self.title

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())
