class Stationery:
    title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print('Запуск отрисовки ' + self.title)

class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print('Запуск отрисовки ' + self.title)

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print('Запуск отрисовки ' + self.title)

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
